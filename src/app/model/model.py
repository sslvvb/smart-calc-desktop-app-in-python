# """Фасад модели. Вывает функции всех модулей модели. Cлой бизнес-логики, который вызывает другие слои бизнес-логики"""
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
    def write_history(string_to_write: str) -> list:
        return history.write(string_to_write)

    @staticmethod
    def read_history() -> list:
        return history.read_file()

    @staticmethod
    def clean_history() -> None:
        history.clean()

    @staticmethod
    def get_expression_result(expression: str, x_value: str) -> str:
        if "x" in expression:
            expression = expression.replace("x", x_value)
        result = calculator.calculate(expression)
        if result is not None:
            return result
        else:
            return "Error in expression"
#
# def get_data(self):
#     # Implement data retrieval logic here
#     pass
#
# def process_data(self, data):
#     # Implement data processing logic here
#     pass

# def calculate_graph_expression_result(expression: str, x_min: str, x_max: str) -> Union[list, None]:
#     return calculator.graph_calculate(expression, x_min, x_max)


# def update_config(key: str, value: str) -> bool:
#     key_values: set = {"background", "main_color", "font_size"}
#     if key in key_values:
#         configs.update_config(key, value)
#         return True
#     else:
#         return False
