# """Фасад модели. Вывает функции всех модулей модели. Cлой бизнес-логики, который вызывает другие слои бизнес-логики
# Реализует пттерн фасад"""
from . import calculator
from . import history
from . import configs
from typing import Union


class Model:
    def __init__(self):
        self.data = None

    @staticmethod
    def read_config() -> dict:
        return configs.read_config()

    @staticmethod
    def update_config(key: str, value: str) -> bool:
        key_values: set = {"background", "main_color", "font_size"}
        if key in key_values:
            configs.update_config(key, value)
            return True
        else:
            return False

    @staticmethod
    def get_expression_result(expression: str, x_value: str) -> str:
        if "x" in expression:
            expression = expression.replace("x", x_value)
        result = calculator.calculate(expression)
        if result is not None:
            return result
        else:
            return "Error in expression"

    @staticmethod
    def calculate_graph_expression_result(expression: str, x_min: str, x_max: str) -> Union[list, None]:
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

