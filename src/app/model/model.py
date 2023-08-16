"""Facade class for interacting with different modules of the model.
Implements the facade design pattern."""

from typing import Union

from . import calculator
from . import history
from . import configs


class Model:
    """
    Facade class for interacting with different modules of the model.
    Implements the facade design pattern.
    """

    @staticmethod
    def read_config() -> dict:
        return configs.read_config()

    @staticmethod
    def update_config(key: str, value: str) -> bool:
        allowed_keys: set = {"background", "main_color", "font_size"}
        if key in allowed_keys:
            configs.update_config(key, value)
            return True
        return False

    @staticmethod
    def get_expression_result(expression: str, x_value: str) -> str:
        expression = expression.replace("x", x_value)
        result = calculator.calculate(expression)
        return result if result is not None else "Error in expression"

    @staticmethod
    def calculate_graph_expression_result(
            expression: str, x_min: str, x_max: str
    ) -> Union[list, None]:
        return calculator.graph_calculate(expression, x_min, x_max)

    @staticmethod
    def write_history(string_to_write: str) -> list:
        return history.write(string_to_write)

    @staticmethod
    def read_history() -> list:
        return history.read_file()

    @staticmethod
    def clean_history() -> None:
        history.clean()
