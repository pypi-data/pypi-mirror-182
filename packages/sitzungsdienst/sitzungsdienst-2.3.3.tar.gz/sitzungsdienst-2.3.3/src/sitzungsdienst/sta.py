"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

import asyncio
import io
import re

from PyPDF2 import PdfReader
from PyPDF2._utils import StrByteType

from .models.court import CourtDates
from .models.express import ExpressDates
from .regex import get_court_dates, get_express_dates, get_people
from .utils import data2hash

# Define input data type
Data = StrByteType | bytes


class StA:
    """
    Handles weekly PDF assignments as issued by 'web.sta'
    """

    @staticmethod
    async def run(pdf: list[Data] | Data) -> tuple[CourtDates, ExpressDates]:
        """
        Runs the whole thing - party time!

        :param pdf: list[Data] | Data PDF contents OR filepath(s)
        :return: tuple[CourtDates, ExpressDates]
        """

        # If not list ..
        if not isinstance(pdf, list):
            # .. convert it
            pdf = [pdf]

        # Create data arrays
        court_dates: list[dict[str, str]] = []
        express_dates: list[dict[str, str]] = []

        # Initialize locks
        court_lock = asyncio.Lock()
        dedupe_lock = asyncio.Lock()
        express_lock = asyncio.Lock()

        # Create hash array
        hashes = set()

        # Loop over input data
        for item in pdf:
            # If necessary ..
            if isinstance(item, bytes):
                # .. convert input data
                item = io.BytesIO(item)

            # Create data array
            pages: dict[int, list[str]] = {}

            # Browse pages
            for idx, page in enumerate(PdfReader(item).pages):
                # Retrieve PDF pages
                page: list[str] = [
                    text.strip() for text in page.extract_text().splitlines() if text
                ]

                # If first page ..
                if idx == 0:
                    # .. retrieve express service dates
                    for item in await StA.express(page):
                        # Calculate hash over data
                        express_hash = data2hash(item)

                        # If not processed before ..
                        if express_hash not in hashes:
                            # .. add it
                            # (1) Aquire locks
                            # (2) Store data
                            async with dedupe_lock:
                                hashes.add(express_hash)

                            async with express_lock:
                                express_dates.append(item)

                pages[idx] = page

            # Retrieve court dates
            for item in await StA.process(await StA.extract(pages)):
                # Calculate hash over data
                court_hash = data2hash(item)

                # If not processed before ..
                if court_hash not in hashes:
                    # .. add it
                    # (1) Aquire locks
                    # (2) Store data
                    async with dedupe_lock:
                        hashes.add(court_hash)

                    # Aquire lock
                    async with court_lock:
                        # Store data
                        court_dates.append(item)

        # Remove duplicates
        return CourtDates(court_dates), ExpressDates(express_dates)

    @staticmethod
    def runs(pdf: list[Data] | Data) -> tuple[CourtDates, ExpressDates]:
        """
        Like 'run', but synchronous (not really)

        :param pdf: list[Data] | Data PDF contents OR filepath(s)
        :return: tuple[CourtDates, ExpressDates]
        """

        return asyncio.run(StA.run(pdf))

    @staticmethod
    async def extract(pages: dict[int, list[str]]) -> dict[str, dict[int, list[str]]]:
        """
        Extracts raw data from PDF pages

        :param pages: dict[int, list[str]] PDF pages
        :return: dict Raw source data
        """

        # Create data array
        raw: dict[str, list[str]] = {}

        # Reset weekday buffer
        date: str = ""

        # Extract assignment data
        for page in pages.values():
            # Reset mode
            is_live = False

            for index, text in enumerate(page):
                # Determine starting point ..
                if text == "Anfahrt":
                    is_live = True

                    # .. and proceed with next entry
                    continue

                # Determine terminal point ..
                if text == "Seite":
                    is_live = False

                    # .. and proceed with next entry
                    continue

                # Enforce entries between starting & terminal point
                if not is_live or "Ende der Auflistung" in text:
                    continue

                # Determine current date / weekday
                if text in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]:
                    date = page[index + 1]

                    if date not in raw:
                        raw[date] = []

                    # Proceed with next entry
                    continue

                # Proceed with next entry if it indicates ..
                # (1) .. current date
                if text == date:
                    continue

                # (2) .. follow-up appointment for main trial
                if text in ["F", "+"]:
                    continue

                raw[date].append(text)

        return raw

    @staticmethod
    async def process(raw: dict[str, list[str]]) -> list[dict[str, str]]:
        """
        Processes raw data

        :param raw: dict Raw data
        :return: list[dict[str, str]] Data representing court dates
        """

        # Create data array
        unprocessed: list[tuple[str, str, list[str]]] = []

        # Iterate over source data
        for date, item in raw.items():
            buffer: list[str] = []
            court: str = ""

            # Iterate over text blocks
            for index, text in enumerate(item):
                if is_court(text):
                    court = text

                else:
                    buffer.append(text)

                if index + 1 == len(item) or is_court(item[index + 1]):
                    unprocessed.append((date, court, buffer))

                    # Reset buffer
                    buffer = []

        # Reset global data array
        data: list[dict[str, str]] = []

        for item in unprocessed:
            # Unpack values
            date, court, buffer = item

            # Format data as string
            string = " ".join(buffer)

            # Loop over court dates
            for court_date in get_court_dates(string):
                # Retrieve raw data on assigned people
                people = get_people(court_date["assigned"])

                # Loop over them
                for person in people:
                    # Store data
                    data.append(
                        {
                            "who": person,
                            "date": format_date(date),
                            "when": court_date["time"],
                            "where": format_place(court, court_date["where"]),
                            "what": court_date["docket"],
                            "others": [item for item in people if item != person],
                        }
                    )

        return data

    @staticmethod
    async def express(page: list[str]) -> list[dict[str, str]]:
        """
        Extracts express service dates

        :param page: list[str] PDF page
        :return: list[dict[str, str]] Data representing express service dates
        """

        # Create data array
        express: list[str] = []

        # Detect 'express mode'
        # (1) Activation
        is_express = False

        for text in page:
            # Skip if no express service
            if text == "Keine Einteilung":
                break

            # Determine express service ..
            if text == "Eildienst":
                is_express = True

                # .. and proceed with next entry
                continue

            # Skip
            if text == "Tag":
                break

            if is_express:
                express.append(text)

        # Combine data to string for easier regEx matching
        string = " ".join(express)

        # Create data buffer
        data: list[dict[str, str]] = []

        # Loop over express service dates
        for express_date in get_express_dates(string):
            # Retrieve raw data on assigned people
            people = get_people(express_date["assigned"])

            # Loop over them
            for person in people:
                # Store data
                data.append(
                    {
                        "start": format_date(express_date["start"]),
                        "end": format_date(express_date["end"]),
                        "who": person,
                        "others": [item for item in people if item != person],
                    }
                )

        return data


def is_court(string: str) -> bool:
    """
    Checks whether string denotes district or regional court

    :param string: str String to be checked
    :return: bool Whether or not string denotes a court
    """

    if re.match(r"(?:AG|LG)\s", string.strip()):
        return True

    return False


def format_date(string: str) -> str:
    """
    Formats (german) date format DIN 1355-1 to ISO 8601

    :param string: str String representing date
    :return: str Formatted date
    """

    return "-".join(reversed(string.split(".")))


def format_place(court: str, extra: str) -> str:
    """
    Formats court & additional information

    :param court: str String representing a court
    :param extra: str String holding additional information
    :return: str Formatted place
    """

    # Format string representing court
    string = court.replace(" ,", "").strip()

    return f"{string} {extra.strip()}" if extra else string
