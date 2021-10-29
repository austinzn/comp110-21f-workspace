"""Utility functions."""

__author__ = "730466197"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # Close the file and we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a column-based table with only a select number of rows of data for each column."""
    result: dict[str, list[str]] = {}
    i: int = 0 
    for key in table:
        values: list[str] = []
        while i < n:
            values.append(table[key][i])
            result[key] = values
            i += 1
        i = 0
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only a subset of the original columns."""
    result: dict[str, list[str]] = {}
    i = 0
    while i < len(names):
        result[names[i]] = table[names[i]]
        i += 1
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column-based tables into one."""
    result: dict[str, list[str]] = {}
    for key in table_one:
        result[key] = table_one[key]
    for key in table_two:
        if key in result:
            result[key] += table_two[key]
        else:
            result[key] = table_two[key]
    return result


def count(list: list[str]) -> dict[str, int]:
    """Count the number of appearances each value makes in a list."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(list):
        if list[i] in result:
            result[list[i]] += 1
        else:
            result[list[i]] = 1
        i += 1
    return result