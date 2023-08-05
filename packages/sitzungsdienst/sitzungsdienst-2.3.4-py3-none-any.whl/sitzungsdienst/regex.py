"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

import re


def _get_data(regex: re.Pattern, string: str) -> list[dict[str, str]]:
    """
    Retrieves data

    :param regex: re.Pattern Compiled regex
    :param string: str String
    :return: list[dict[str, str]] Data
    """

    # Retrieve data
    # (1) Match pattern
    # (2) Clean strings
    return [
        {k: v.strip() for k, v in match.groupdict().items()}
        for match in regex.finditer(string)
    ]


COURT_DATES = re.compile(
    r"""
    # (1) .. location (optional)
    (?P<where>(?:.*?)?)\s?
    # (2) .. time of court date
    (?P<time>\d{2}:\s?\d{2})\s
    # (3) .. docket number
    (?P<docket>\d{2,3}\sU?Js\s\d+\/\d{2})\s
    # (4) .. name(s) of prosecutor(s), namely ..
    (?P<assigned>
        (?:
            # (a) .. last name & doctoral degree (optional)
            (?:(?:Dr\.\s)?[\u00C0-\u017F\w-]+)
            # (b) .. department number (optional)
            (?:\s?(?:\([0-9XIV]+\)))?\s?,\s
            # (c) .. first name
            (?:[\u00C0-\u017F\w-]+)\s?,\s
            # (d) .. official title
            (?:
                (?:
                    Ref|JOI|AAAnw|
                    E?(?:O?StA|O?AA)|
                    (?:RR(?:\'in)?aAA)
                )
                (?:\'in)?
                (?:\s\(ba\))?
            )\s?
        )+
    )
    """,
    re.VERBOSE,
)


def get_court_dates(string: str) -> list[dict[str, str]]:
    """
    Retrieves data representing court dates

    :param string: str String representing court dates
    :return: list[dict[str, str]] Data representing court dates
    """

    return _get_data(COURT_DATES, string)


EXPRESS_DATES = re.compile(
    r"""
    # (1) .. start date
    (?P<start>\d{2}\.\d{2}\.\d{4})\s
    # (2) .. hyphen, followed by whitespace
    (?:-\s)
    # (3) .. end date
    (?P<end>\d{2}\.\d{2}\.\d{4})\s
    # (4) .. name(s) of prosecutor(s), namely ..
    (?P<assigned>
        (?:
            # (a) .. last name & doctoral degree (optional)
            (?:(?:Dr\.\s)?[\u00C0-\u017F\w-]+)
            # (b) .. department number (optional)
            (?:\s(?:\([0-9XIV]+\)))?\s?,\s
            # (c) .. first name
            (?:[\u00C0-\u017F\w-]+)\s?,\s
            # (d) .. official title
            (?:
                (?:
                    Ref|JOI|AAAnw|
                    E?(?:O?StA|O?AA)|
                    (?:RR(?:\'in)?aAA)
                )
                (?:\'in)?
                (?:\s\(ba\))?
            )\s?
        )+
    )
    """,
    re.VERBOSE,
)


def get_express_dates(string: str) -> list[dict[str, str]]:
    """
    Retrieves data representing express service dates

    :param string: str String representing express service dates
    :return: list[dict[str, str]] Data representing express service dates
    """

    return _get_data(EXPRESS_DATES, string)


PERSON = re.compile(
    r"""
    # (1) .. doctoral degree (optional)
    (?P<doc>(?:Dr\.)?)\s??
    # (2) .. last name
    (?P<last>[\u00C0-\u017F\w-]+)\s?
    # (3) .. department number (optional)
    (?P<department>(?:\([0-9XIV]+\))?)\s?,\s?
    # (4) .. first name
    (?P<first>[\u00C0-\u017F\w-]+)\s?,\s?
    # (5) .. official title, being either ..
    (?P<title>
        (?:
            # (a) .. Rechtsreferendar:in
            # - Ref / Ref'in
            #
            # (b) .. Justizoberinspektor:in
            # - JOI / JOI'in
            #
            # (c) .. Amtsanwaltsanwärter:in
            # - AAAnw / AAAnw'in
            Ref|JOI|AAAnw|

            # (d) .. (Erste:r / Ober-) Staatsanwalt:anwältin
            # - OStA / OStA'in
            # - EStA / EStA'in
            # - StA / StA'in
            # (e) .. (Erste:r) (Oberamts-) Anwalt:Anwältin
            # - EOAA / EOAA'in
            # - OAA / OAA'in
            E?(?:O?StA|O?AA)|

            # (f) .. Regierungsrat:rätin als Amtsanwalt:anwältin
            # - RRaAA / RR'inaAA'in
            (?:RR(?:\'in)?aAA)
        )
        (?:\'in)?
        (?:\s\(ba\))?
    )
    """,
    re.VERBOSE,
)


def get_people(string: str) -> list[dict[str, str]]:
    """
    Retrieves data representing assigned people

    :param string: str String representing assigned people
    :return: list[dict[str, str]] Data representing people
    """

    return _get_data(PERSON, string)
