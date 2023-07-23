"""Модуль для работы с историей выражений."""

from pathlib import Path
from django.conf import settings

# HISTORY_PATH: str = "data/history.txt"

def read_file() -> list:
    """Чистает историю запросов из файла history.txt

    Returns:
        list: Список из введенных выражений и значения x.
    """
    Path(settings.DATA_FILE_PATH).touch(exist_ok=True)
    with open(settings.DATA_FILE_PATH, 'r', encoding='utf-8') as file:
        return file.readlines()


def clean() -> None:
    """Очищает историю запросов в файле history.txt

    Returns:
        list: Пустой список введенных выражений.
    """
    Path(settings.DATA_FILE_PATH).touch(exist_ok=True)
    with open(settings.DATA_FILE_PATH, 'r+', encoding='utf-8') as file:
        file.truncate(0)


def write(record_line: str) -> list:
    """Добавляет новый запрос в файл с историей запросов history.txt

    Returns:
        list: Обновленный список из введенных выражений и значения x.
    """
    Path(settings.DATA_FILE_PATH).touch(exist_ok=True)
    with open(settings.DATA_FILE_PATH, 'r', encoding='utf-8') as file:
        file_lines: list = file.readlines()
    with open(settings.DATA_FILE_PATH, 'w', encoding='utf-8') as file:
        file.write(record_line + '\n')
        file.writelines([line for line in file_lines])
    with open(settings.DATA_FILE_PATH, 'r', encoding='utf-8') as file:
        return file.readlines()
