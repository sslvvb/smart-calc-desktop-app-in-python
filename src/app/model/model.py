"""
Facade class for interacting with different modules of the model.
Implements the facade design pattern.
"""

from typing import Union

from . import calculator
from . import history
from . import configs


class Model:
    """
    Facade class for interacting with different modules of the model.
    """

    @staticmethod
    def read_config() -> dict:
        """
        Reads the configuration data.

        Returns:
            dict: Configuration data.
        """
        return configs.read_config()

    @staticmethod
    def update_config(key: str, value: str) -> bool:
        """
        Updates the configuration with a new key-value pair.

        Args:
            key (str): Key to update.
            value (str): New value to set.

        Returns:
            bool: True if the key is valid and updated successfully, else False.
        """
        allowed_keys: set = {'background', 'main_color', 'font_size'}
        if key in allowed_keys:
            configs.update_config(key, value)
            return True
        return False

    @staticmethod
    def get_expression_result(expression: str, x_value: str) -> str:
        """
        Calculates the result of an expression with a given x value.

        Args:
            expression (str): Mathematical expression.
            x_value (str): Value of x.

        Returns:
            str: Result of the expression or an error message.
        """
        expression: str = expression.replace('x', x_value)
        result: Union[str, None] = calculator.calculate(expression)
        return result if result is not None else 'Error in expression'

    @staticmethod
    def calculate_graph_expression_result(
            expression: str, x_min: str, x_max: str
    ) -> Union[list, None]:
        """
        Calculates the result of a graph expression over a range of x values.

        Args:
            expression (str): Graph expression.
            x_min (str): Minimum value of x.
            x_max (str): Maximum value of x.

        Returns:
            Union[list, None]: List of calculated values or None if an error
            occurred.
        """
        return calculator.graph_calculate(expression, x_min, x_max)

    @staticmethod
    def write_history(string_to_write: str) -> list:
        """
        Writes a string to the history.

        Args:
            string_to_write (str): String to write.

        Returns:
            list: Updated history.
        """
        return history.write(string_to_write)

    @staticmethod
    def read_history() -> list:
        """
        Reads the history data.

        Returns:
            list: List of historical data.
        """
        return history.read_file()

    @staticmethod
    def clean_history() -> None:
        """
        Cleans the history data.
        """
        history.clean()
