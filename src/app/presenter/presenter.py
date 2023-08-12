from typing import Union


class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.init_ui(self, self.model.read_config())
        # self.view.set_history(self.model.read_history())
        self.view.mainloop()

    def handle_update_config(self, key: str, value: str):
        if self.model.update_config(key, value):
            self.view.update_config(key, value)
            # logger.info(f'{log_message} to {setting_value}')
        else:
            # logger.warning(f'Failed to {log_message} to {setting_value}')
            pass

    def handle_expression_result(self, expression: str, x_value: str) -> None:
        result = self.model.get_expression_result(expression, x_value)
        # if result != "Error in expression":
        #     self.model.write_history(f'{expression}={result}; x={x_value}')
        # обновить историю на экране
        self.view.set_expression_result(result)
        # logger.info(f'{expression}={result}; x={x_value}')

    def handle_graphic_result(self, expression: str, x_min: str, x_max: str) -> None:
        result: Union[list, None] = self.model.calculate_graph_expression_result(expression, x_min, x_max)
        if result is None:
            self.view.set_expression_result('Error in expression')
            #  logger.warning(f'Error in expression for graph: {expression}')
        else:
            self.view.add_graph(result)
            # logger.info

    def handle_delete_history(self):
        pass
    #     self.model.clean_history()
    #     # self.view.set_history(self.model.read_history())  # надо ??
    #
    # # def handle_user_action(self):
    # #     data = self.view.get_user_input()
    # #     result = self.model.perform_operation(data)
    # #     self.view.update_result(result)
