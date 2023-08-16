"""Модуль для работы с историей выражений."""

import os
from pathlib import Path

current_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)))
_HISTORY_PATH = os.path.join(current_directory, 'data/history.txt')


def read_file() -> list:
    """Чистает историю запросов из файла history.txt

    Returns:
        list: Список из введенных выражений и значения x.
    """
    Path(_HISTORY_PATH).touch(exist_ok=True)
    with open(_HISTORY_PATH, 'r', encoding='utf-8') as file:
        return file.readlines()


def clean() -> None:
    """Очищает историю запросов в файле history.txt

    Returns:
        list: Пустой список введенных выражений.
    """
    Path(_HISTORY_PATH).touch(exist_ok=True)
    with open(_HISTORY_PATH, 'r+', encoding='utf-8') as file:
        file.truncate(0)


def write(record_line: str) -> list:
    """Добавляет новый запрос в файл с историей запросов history.txt

    Returns:
        list: Обновленный список из введенных выражений и значения x.
    """
    Path(_HISTORY_PATH).touch(exist_ok=True)
    with open(_HISTORY_PATH, 'r', encoding='utf-8') as file:
        file_lines: list = file.readlines()
    with open(_HISTORY_PATH, 'w', encoding='utf-8') as file:
        file.write(record_line + '\n')
        file.writelines([line for line in file_lines])
    with open(_HISTORY_PATH, 'r', encoding='utf-8') as file:
        return file.readlines()
