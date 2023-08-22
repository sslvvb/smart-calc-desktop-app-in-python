"""Module for working with expression history."""

import os
from pathlib import Path

_HISTORY_PATH: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data/history.txt"
)


def read_file() -> list:
    """
    Read and return the history from the history file.

    Returns:
        list: List of entered expressions, x values and result.
    """
    Path(_HISTORY_PATH).touch(exist_ok=True)
    with open(_HISTORY_PATH, "r", encoding="utf-8") as file:
        return file.readlines()


def clean() -> None:
    """
    Clear the history of expressions in the history file.
    """
    Path(_HISTORY_PATH).touch(exist_ok=True)
    with open(_HISTORY_PATH, "r+", encoding="utf-8") as file:
        file.truncate(0)


def write(record_line: str) -> list:
    """
    Add a new expression to the history file.

    Args:
        record_line (str): Expression to add.

    Returns:
        list: Updated list of entered expressions, x values and result.
    """
    Path(_HISTORY_PATH).touch(exist_ok=True)
    with open(_HISTORY_PATH, "r", encoding="utf-8") as file:
        file_lines: list = file.readlines()
    with open(_HISTORY_PATH, "w", encoding="utf-8") as file:
        file.write(record_line + "\n")
        file.writelines(file_lines)
    with open(_HISTORY_PATH, "r", encoding="utf-8") as file:
        return file.readlines()
