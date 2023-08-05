# sitzungsdienst
[![License](https://badgen.net/badge/license/GPL/blue)](https://codeberg.org/S1SYPHOS/sitzungsdienst/src/branch/main/LICENSE) [![PyPI](https://badgen.net/pypi/v/sitzungsdienst)](https://pypi.org/project/sitzungsdienst) [![Coverage](https://badgen.net/badge/coverage/100/cyan)](https://codeberg.org/S1SYPHOS/sitzungsdienst/src/branch/main/COVERAGE) [![Build](https://ci.codeberg.org/api/badges/S1SYPHOS/sitzungsdienst/status.svg)](https://codeberg.org/S1SYPHOS/sitzungsdienst/issues)

A simple Python utility for working with weekly assignment PDFs as exported by [`web.sta`](https://www.dvhaus.de/leistungen/web.sta).


## Getting started

Simply install all dependencies inside a virtual environment to get started:

```bash
# Clone repository & change directory
git clone https://codeberg.org/S1SYPHOS/sitzungsdienst && cd sitzungsdienst

# Set up & activate virtualenv
poetry shell

# Install dependencies
poetry install
```


## Usage

Using this library is straightforward:

```python
from sitzungsdienst import StA

# Pass file path (or its stream) & retrieve data
court_dates, express_dates = StA.runs('path/to/file.pdf')

# You may also pass multiple file paths (or their streams)
court_dates, express_dates = StA.runs(['path/to/file1.pdf', 'path/to/file2.pdf'])

# Use a subset by filtering it
filtered_court = court_dates.filter(['alice', 'bob'])
filtered_express = express_dates.filter('john')

# Get iCalendar data
ics = filtered_court.data2ics()
print(ics)

##
# BEGIN:VCALENDAR
# VERSION:2.0
# ..
# ..
```

**Note**: Since all data methods are using `async`, you should either `await` them (inside your own `asyncio` context) or call them using `asyncio.run()` (see below).

```python
import asyncio
from sitzungsdienst import StA

async def main(file):
    # ..

    return await StA.run(file)

# Retrieve data
data = asyncio.gather(*[main(file) for file in files])

# ..
```

If you want to see it in action, head over to the [`sitzungsapp`](https://codeberg.org/S1SYPHOS/sitzungsapp)!


**Happy coding!**
