import customtkinter

from .main_buttons import MainButtons
from presenter import presenter


class View(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Calculator")
        self.geometry("1300x700")

        self.main_buttons = MainButtons(self)
        self.main_buttons.grid(row=0, column=0, sticky="nsw")

    def init_ui(self, presenter: presenter.Presenter):
        self.main_buttons.init_ui(presenter)

    def set_expression_result(self, res: str) -> None:
        self.main_buttons.set_expression_result(res)


