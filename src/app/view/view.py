"""
The main view module of the Smart Calculator application.
"""

import customtkinter as ctk
import matplotlib.pyplot as plt

from .utils import get_code_bg_color, get_code_main_color
from .error import Error
from .about import About
from .ui_initializer import UiInitializer


class View(ctk.CTk):
    """The main View class responsible for the user interface."""

    def __init__(self):
        super().__init__()
        self.title("Smart Calculator")
        self.geometry("865x390")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.ui_initializer = UiInitializer(self)
        self.presenter = None

        self.main_color = None
        self.background = None
        self.font_size = None
        self.history = None
        self.history_menu = None
        self.buttons = []
        self.radio_buttons = []

        self.expression_var = ctk.StringVar()
        self.x_var = ctk.StringVar()
        self.x_min_var = ctk.StringVar()
        self.x_max_var = ctk.StringVar()
        self.y_min_var = ctk.StringVar()
        self.y_max_var = ctk.StringVar()

        self.error_window = None
        self.about_window = None

    def init_ui(self, presenter, config: dict, history: list) -> None:
        self.presenter = presenter
        self.main_color = config["main_color"]
        self.background = config["background"]
        self.font_size = config["font_size"]
        self.history = history
        self.ui_initializer.init()

    def update_config(self, key: str, value: str):
        self.ui_initializer.update_config(key, value)

    def config_event_callback(self, key: str, value: str) -> None:
        self.presenter.handle_update_config(key, value)

    def on_button_click(self, button_text):
        if button_text == "GRAPH":
            self.graph_button_callback()
        elif button_text == "AC":
            self.expression_var.set("")
        elif button_text == "=":
            self.presenter.handle_expression_result(
                self.expression_var.get(), str(self.x_var.get())
            )
        elif button_text == "Delete history":
            self.presenter.handle_delete_history()
        elif button_text == "About app":
            self._show_about_app()
        else:
            self.append_to_expression(button_text)

    def graph_button_callback(self) -> None:
        if self._check_coordinates():
            self.presenter.handle_graphic_result(
                self.expression_var.get(), self.x_min_var.get(),
                self.x_max_var.get()
            )
        else:
            self._show_error_message(
                "Error in expression or coordinate values.")

    def _check_coordinates(self) -> bool:
        if (
                self.expression_var.get() != ""
                and self.x_min_var.get() != ""
                and self.x_max_var.get() != ""
                and self.y_min_var.get() != ""
                and self.y_max_var.get() != ""
        ):
            if float(self.x_min_var.get()) < float(
                    self.x_max_var.get()) and float(
                    self.y_min_var.get()
            ) < float(self.y_max_var.get()):
                return True
        return False

    def _show_error_message(self, message: str) -> None:
        if self.error_window is None or not self.error_window.winfo_exists():
            self.error_window = Error(
                self, message=message,
                background=get_code_bg_color(self.background)
            )
        else:
            self.error_window.focus()

    def _show_about_app(self):
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = About(
                self, background=get_code_bg_color(self.background)
            )
        else:
            self.about_window.focus()

    def append_to_expression(self, text):
        current_expression = self.expression_var.get()
        if len(current_expression) + len(text) <= 255:
            new_expression = current_expression + text
            self.expression_var.set(new_expression)

    def history_menu_callback(self, choice):
        if choice != "No History":
            history_item = choice.rstrip()
            split_lines: list = history_item.split("=")
            self.expression_var.set(split_lines[0])
            self.x_var.set(split_lines[2])

    def update_history(self, history: list):
        self.history = history
        self.history_menu.configure(values=self._history_menu_values())
        if self.history:
            self.history_menu.set(self.history[0])
        else:
            self.history_menu.set("No History")

    def _history_menu_values(self):
        return self.history if self.history else ["No History"]

    def set_font_size(self, font_size: str) -> None:
        font = ("Helvetica", int(font_size))
        for widget in self.winfo_children():
            widget.configure(font=font)

    def add_graph(self, result: list):
        fig, ax = plt.subplots(facecolor=get_code_bg_color(self.background))  # pylint: disable=unused-variable
        plt.scatter(
            result[0],
            result[1],
            marker=".",
            color=get_code_main_color(self.main_color),
            linewidth=2,
        )
        plt.ylim(float(self.y_min_var.get()), float(self.y_max_var.get()))
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_title(self.expression_var.get())
        plt.grid(True)
        plt.show()

    def set_expression_result(self, res: str) -> None:
        self.expression_var.set(res)
