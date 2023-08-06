class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run_app(self):
        self.view.mainloop()

    def handle_user_action(self):
        data = self.view.get_user_input()
        result = self.model.perform_operation(data)
        self.view.update_result(result)
