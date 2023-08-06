![](http://ForTheBadge.com/images/badges/made-with-python.svg)

# PyScalix

A package to convert csv files to sqlite database and sqlite database to csv files

## Functions

- tocsv
- tosqlite

## Usage/Examples

```python
from PyScalix.toCsv import SqliteToCsv
SqliteToCsv.tocsv()

from PyScalix.toSqlite import CsvToSqlite
CsvToSqlite.tosqlite()

```

```
tosqlite() takes two parameters
```

- Database file
- Table name

```
toCsv() takes one parameter
```

- Database file

## Success Response

- True

## Error Response

- False

## Tech Stack

**Language:** Python 3.10.9

## Authors

- [Husnain Khurshid](https://www.github.com/mhusnainkh)
- [Usman Sadiq](https://www.github.com/usman-cs)
