"""Module for the Presenter class that handles user interactions and data presentation."""  # pylint: disable=line-too-long

import os
import logging
from typing import Union
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


class Presenter:
    """Class responsible for handling user interactions and presenting data."""

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.logger = setup_logging("H")

    def run(self):
        self.logger.info("Start app")
        self.view.init_ui(self, self.model.read_config(),
                          self.model.read_history())
        self.view.mainloop()

    def handle_update_config(self, key: str, value: str):
        if self.model.update_config(key, value):
            self.view.update_config(key, value)
            self.logger.info("Change %s to %s", key, value)
        else:
            self.logger.warning("Failed to change %s to %s", key, value)

    def handle_expression_result(self, expression: str, x_value: str) -> None:
        result = self.model.get_expression_result(expression, x_value)
        if result != "Error in expression":
            self.logger.info("CALCULATE %s=%s; x=%s", expression, result,
                             x_value)
            new_history: list = self.model.write_history(
                f"{expression}={result}; x={x_value}"
            )
            self.view.update_history(new_history)
        else:
            self.logger.warning("Error in expression: %s; x=%s", expression,
                                x_value)
        self.view.set_expression_result(result)

    def handle_graphic_result(self, expression: str, x_min: str,
                              x_max: str) -> None:
        result: Union[
            list, None] = self.model.calculate_graph_expression_result(
            expression, x_min, x_max
        )
        if result is None:
            self.view.set_expression_result("Error in expression")
            self.logger.warning("Error in expression for graph: %s", expression)
        else:
            self.view.add_graph(result)
            self.logger.info("GRAPH SUCCESS: %s", expression)

    def handle_delete_history(self):
        self.model.clean_history()
        self.view.update_history(self.model.read_history())
        self.logger.info("delete history.txt")


def setup_logging(log_rotation_period):
    current_directory = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir
    )
    log_dir = os.path.join(current_directory, "logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_format = "logs_%d-%m-%Y-%H-%M-%S.log"
    log_file_path = os.path.join(log_dir,
                                 datetime.now().strftime(log_file_format))

    rotation_logging_handler = TimedRotatingFileHandler(
        log_file_path, when=log_rotation_period, interval=1
    )
    rotation_logging_handler.setFormatter(
        logging.Formatter(fmt="[%(asctime)s: %(levelname)s] %(message)s")
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(rotation_logging_handler)

    return logger
