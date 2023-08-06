import tkinter as tk

# Model
class AppModel:
    def multiply_by_two(self, number):
        return number * 2

# View
class AppView:
    def __init__(self, root):
        self.root = root

        self.number_entry = tk.Entry(self.root)
        self.number_entry.pack()

        self.multiply_button = tk.Button(self.root, text="Multiply by 2", command=self.handle_multiply)
        self.multiply_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def get_user_input(self):
        return int(self.number_entry.get())

    def update_result(self, result):
        self.result_label.config(text=f"Result: {result}")

    def set_presenter(self, presenter):
        self.presenter = presenter

    def handle_multiply(self):
        self.presenter.handle_multiply()

# Presenter
class AppPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_presenter(self)

    def handle_multiply(self):
        user_input = self.view.get_user_input()
        result = self.model.multiply_by_two(user_input)
        self.view.update_result(result)

# Main application code
if __name__ == "__main__":
    root = tk.Tk()
    root.title("MVP Example")

    model = AppModel()
    view = AppView(root)
    presenter = AppPresenter(model, view)

    root.mainloop()
