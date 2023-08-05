"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
import copy
from dataclasses import asdict, dataclass
import datetime
from operator import attrgetter
from typing import Any, Sequence

import ics  # type: ignore


@dataclass
class Date:
    """
    Base class for single assignment
    """

    # Assigned person
    who: dict[str, str]

    # Assigned people (other than 'who')
    others: list[dict[str, str]]

    def to_dict(self) -> dict[str, Any]:
        """
        Exports data

        :return: dict[str, Any]
        """

        return asdict(self)

    @property
    def name(self) -> str:
        """
        Builds full name (including title & department)

        :return: str Full name
        """

        return format_person(self.who)

    @property
    def name2sort(self) -> str:
        """
        Provides name key to sort by (last name, first name)

        :return: str Name sort key
        """

        return f'{self.who["last"]}, {self.who["first"]}'

    @property
    def assigned(self) -> str:
        """
        Builds full name (including title & department) of all assigned

        :return: str Full name(s)
        """

        # If only one assignee ..
        if not self.others:
            # .. provide its name
            return self.name

        # Provide all assignees
        return "; ".join([self.name, format_people(self.others)])


class Dates(ABC):
    """
    Base class for multiple assignments
    """

    # Assignment data
    data: Sequence[Date]

    # Sort order
    sort_order: list[str] = []

    # Event host (ICS only)
    creator: str = "S1SYPHOS"

    # Preferred timezone (ICS only)
    timezone: str = "Europe/Berlin"

    def __iter__(self):  # type: ignore
        """
        Enables iteration
        """

        yield from self.data

    def __len__(self) -> int:
        """
        Enables 'len()'

        :return: int
        """

        return len(self.data)

    def to_dict(self) -> list[dict[str, Any]]:
        """
        Exports assignment data

        :return: list[dict[str, Any]]
        """

        return self.sort(self.data)

    def filter(self, query: list[str] | str) -> list[dict[str, Any]]:
        """
        Filters assignments by search term(s)

        :param query: List[str] | str Search terms
        :return: list[dict[str, Any]] Filtered assignments
        """

        # If query represents string ..
        if isinstance(query, str):
            # .. make it a list
            query = [query]

        # Create data buffer
        dates: list[dict[str, str]] = []

        # Loop over search terms in order to ..
        for term in query:
            # .. filter out relevant items
            dates.extend(
                [
                    item
                    for item in copy.deepcopy(self.data)
                    if term.lower() in item.name.lower()
                ]
            )

        return self.sort(dates)

    def sort(self, dates: list[Date]) -> list[dict[str, Any]]:
        """
        Sorts dates

        :param dates: list[Date] Unsorted dates
        :return: list[dict[str, Any]] Sorted dates
        """

        # Sort data
        dates.sort(key=attrgetter(*self.sort_order))

        return [item.to_dict() for item in dates]

    @abstractmethod
    def data2ics(self) -> ics.Calendar:
        """
        Exports assignments as ICS calendar object

        :return: ics.Calendar
        """

    # HELPERS

    def to_time(self, date_time: str, fmt: str = "%Y-%m-%d") -> datetime.datetime:
        """
        Datetime object helper

        :param date_time: str Date and/or time
        :param fmt: str Datetime pattern
        :return: datetime.datetime
        """

        return datetime.datetime.strptime(date_time, fmt)

    def add_attendees(self, date: Date, event: ics.Event) -> None:
        """
        Adds people as attendees to event

        :param date: Date Date object
        :param event: ics.Event Attended event
        :return: None
        """

        def add(person: dict[str, str], event: ics.Event):
            """
            Adds person as attendee to event

            :param dict[str, str]: Attending person
            :param event: ics.Event Attended event
            :return: None
            """

            # Build attendee
            attendee = ics.Attendee("")

            # Edit name (= title, full name & department)
            attendee.common_name = format_person(person)

            # Add to assignment
            event.add_attendee(attendee)

        # Add assigned person
        add(date.who, event)

        # Add remaining people
        for person in date.others:
            add(person, event)


def format_person(person: dict[str, str]) -> str:  # type: ignore
    """
    Formats single person

    :param person: dict[str, str] Data representing assigned person
    :return: str Formatted person
    """

    return " ".join(
        [
            string.strip()
            for string in [
                person["title"],
                person["doc"],
                person["first"],
                person["last"],
                person["department"],
            ]
            if string
        ]
    )


def format_people(people: list[dict[str, str]]) -> str:
    """
    Formats assigned people

    :param people: list[dict[str, str]] Data representing assigned people
    :return: str Formatted people
    """

    # Bring people together
    return "; ".join([format_person(person) for person in people])
