class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.init_ui(self)
        # self.view.set_history(self.model.read_history())
        # set config
        self.model.read_config()
        self.view.mainloop()

    def handle_expression_result(self, expression: str, x_value: str) -> None:
        result = self.model.get_expression_result(expression, x_value)
        if result != "Error in expression":
            self.model.write_history(f'{expression}={result}; x={x_value}')
            # обновить историю на экране # TODO
        self.view.set_expression_result(result)
        # logger.info(f'{expression}={result}; x={x_value}')  # TODO

    def handle_delete_history(self):
        self.model.clean_history()
        # self.view.set_history(self.model.read_history())  # надо ??

    # def handle_user_action(self):
    #     data = self.view.get_user_input()
    #     result = self.model.perform_operation(data)
    #     self.view.update_result(result)
