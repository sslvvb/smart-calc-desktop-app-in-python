class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.init_ui(self)
        self.view.mainloop()

    def handle_expression_result(self, expression: str, x_value: str) -> None:
        res = self.model.get_expression_result(expression, x_value)
        print(res)
        self.view.set_expression_result(res)
        pass

    def handle_delete_history(self):
        self.model

    # def handle_user_action(self):
    #     data = self.view.get_user_input()
    #     result = self.model.perform_operation(data)
    #     self.view.update_result(result)
