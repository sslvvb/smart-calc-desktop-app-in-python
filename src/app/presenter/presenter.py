import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
from typing import Union


class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._logger = logging.getLogger(__name__)
        self._init_logger()

    def run(self):
        self.view.init_ui(self, self.model.read_config())
        # self.view.set_history(self.model.read_history())
        self.view.mainloop()
        self._logger.info("Start app")

    def handle_update_config(self, key: str, value: str):
        if self.model.update_config(key, value):
            self.view.update_config(key, value)
            self._logger.info(f'Change {key} to {value}')
        else:
            self._logger.warning(f'Failed to change {key} to {value}')

    def handle_expression_result(self, expression: str, x_value: str) -> None:
        result = self.model.get_expression_result(expression, x_value)
        # if result != "Error in expression":
        #     self.model.write_history(f'{expression}={result}; x={x_value}')
        # обновить историю на экране
        self.view.set_expression_result(result)
        self._logger.info(f'CALCULATE {expression}={result}; x={x_value}')

    def handle_graphic_result(self, expression: str, x_min: str, x_max: str) -> None:
        result: Union[list, None] = self.model.calculate_graph_expression_result(expression, x_min, x_max)
        if result is None:
            self.view.set_expression_result('Error in expression')
            self._logger.warning(f'Error in expression for graph: {expression}')
        else:
            self.view.add_graph(result)
            self._logger.info(f'Success expression to graph: {expression}')

    def handle_delete_history(self):
        pass  # logger

    #     self.model.clean_history()
    #     # self.view.set_history(self.model.read_history())  # надо ?? # logger
    #
    # # def handle_user_action(self): # logger
    # #     data = self.view.get_user_input()
    # #     result = self.model.perform_operation(data)
    # #     self.view.update_result(result)

    def _init_logger(self):
        rotation_logging_handler = TimedRotatingFileHandler('app/logs/log.log', when='m', interval=1)
        rotation_logging_handler.suffix = '%Y%m%d'
        rotation_logging_handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(rotation_logging_handler)
