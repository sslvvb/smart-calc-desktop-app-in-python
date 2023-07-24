"""Фасад модели. Вывает функции всех модулей модели. Cлой бизнес-логики, который вызывает другие слои бизнес-логики"""

from . import calculator
from . import history
from . import configs
from typing import Union


def read_history() -> list:
    """Вызывает функцию чтения истории введенных выражений модуля history

    Returns:
        list: Список из введенных выражений и значения x.
    """
    return history.read_file()


def write_history(string_to_write: str) -> list:
    """Вызывает функцию, добавляющую запрос в историю выражений модуля history

    Returns:
        list: Обновленный список из введенных выражений.
    """
    return history.write(string_to_write)


def clean_history() -> None:
    """Вызывает функцию очищения истории введенных выражений модуля history

    Returns:
        list: Пустой список введенных выражений.
    """
    history.clean()


def get_expression_result(expression: str, x_value: str) -> str:
    """вызывает функцию
    Вычисляет выражение. Возвращает строку - результат вычислений или текст ошибки.
    параметры - выражение, значениие х"""
    if "x" in expression:
        expression = expression.replace("x", x_value)
    result = calculator.calculate(expression)
    if result is not None:
        return result
    else:
        return "Error in expression"


def calculate_graph_expression_result(expression: str, x_min: str, x_max: str) -> Union[list, None]:
    return calculator.graph_calculate(expression, x_min, x_max)


def read_config() -> dict:
    return configs.read_config()


def update_config(key: str, value: str) -> bool:
    key_values: set = {"background", "main_color", "font_size"}
    if key in key_values:
        configs.update_config(key, value)
        return True
    else:
        return False

