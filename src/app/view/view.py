import customtkinter as ctk
import matplotlib.pyplot as plt

from .graphic import Graphic
from presenter.presenter import Presenter


class View(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Calculator")
        self.geometry("865x390")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.buttons = []
        self.radio_buttons = []
        self.presenter = None
        self.toplevel_window = None
        self.main_color = None
        self.background = None
        self.font_size = None

        self.expression_var = ctk.StringVar()
        self.x_var = ctk.StringVar()
        self.x_min_var = ctk.StringVar()
        self.x_max_var = ctk.StringVar()
        self.y_min_var = ctk.StringVar()
        self.y_max_var = ctk.StringVar()
        self.history_menu = None

    def init_ui(self, presenter, config) -> None:
        self.presenter = presenter
        self.main_color = config['main_color']
        self.background = config['background']
        self.font_size = config['font_size']
        self.init_config()
        self.init_entry()
        self.init_buttons()
        self.init_history()
        self.init_label()
        self.configure_children()
        self.configure(fg_color=self.get_code_bg_color(self.background))
        self.set_font_size(self.font_size)

    def init_config(self):
        self.init_radio_buttons('main_color', ['pink', 'green'], row=9)
        self.init_radio_buttons('background', ['light', 'dark'], row=10)
        self.init_radio_buttons('font_size', ['14', '16'], row=11)

    def init_radio_buttons(self, key, values, row):
        var = ctk.StringVar(value=getattr(self, key))
        for idx, value in enumerate(values, start=1):
            radio = ctk.CTkRadioButton(self, text=value,
                                       command=lambda k=key, v=value: self.config_event_callback(k, v),
                                       variable=var, value=value, border_color='#343230', hover_color='#343230',
                                       text_color='#343230', fg_color=self.get_code_main_color(self.main_color))
            radio.grid(row=row, column=idx, columnspan=1)
            self.radio_buttons.append(radio)

    def config_event_callback(self, key: str, value: str) -> None:
        self.presenter.handle_update_config(key, value)

    def get_code_main_color(self, color: str) -> str:
        color_map = {'pink': '#F099B1', 'green': '#85DABB'}
        return color_map.get(color, '')

    def get_code_bg_color(self, color_mode: str) -> str:
        color_map = {'light': '#f8f8f8', 'dark': '#CCCCCC'}
        return color_map.get(color_mode, '')

    def set_font_size(self, font_size: str) -> None:
        font = ("Helvetica", int(font_size))
        for widget in self.winfo_children():
            widget.configure(font=font)

    def update_config(self, key: str, value: str):
        if key == 'main_color':
            for btn in self.buttons:
                if btn.cget('fg_color') == self.get_code_main_color(self.main_color):
                    btn.configure(fg_color=self.get_code_main_color(value))
            for radio in self.radio_buttons:
                radio.configure(fg_color=self.get_code_main_color(value))
            self.history_menu.configure(fg_color=self.get_code_main_color(value),
                                        button_color=self.get_code_main_color(value))
            self.main_color = value
        if key == 'background':
            self.configure(fg_color=self.get_code_bg_color(value))
            self.background = value
        if key == 'font_size':
            self.set_font_size(value)
            self.font_size = value

    def init_entry(self):
        expression_entry = ctk.CTkEntry(self, textvariable=self.expression_var)
        expression_entry.grid(row=0, column=0, columnspan=6)

        validate_float_command = self.register(self.validate_float_input)

        entry_settings = [
            (self.x_var, "1.0", (1, 2, 3)),
            (self.x_min_var, "-10.0", (7, 1, 2)),
            (self.x_max_var, "10.0", (7, 4, 2)),
            (self.y_min_var, "-10.0", (8, 1, 2)),
            (self.y_max_var, "10.0", (8, 4, 2))
        ]

        for var, initial_value, grid_params in entry_settings:
            var.set(initial_value)
            entry = ctk.CTkEntry(self, textvariable=var, validate="key")
            entry.grid(row=grid_params[0], column=grid_params[1], columnspan=grid_params[2])
            entry.configure(validatecommand=(validate_float_command, '%P'))

    def validate_float_input(self, new_value):
        try:
            if new_value == "" or float(new_value):
                return True
        except ValueError:
            return False
        return False

    def init_buttons(self):
        buttons = [
            ('GRAPH', 1, 0, 'special'), ('x', 1, 1), ('AC', 1, 5, 'special'),
            ('sin', 2, 0), ('asin', 2, 1), ('e', 2, 2), ('(', 2, 3), (')', 2, 4), ('^', 2, 5, 'special'),
            ('cos', 3, 0), ('acos', 3, 1), ('1', 3, 2), ('2', 3, 3), ('3', 3, 4), ('/', 3, 5, 'special'),
            ('tan', 4, 0), ('atan', 4, 1), ('4', 4, 2), ('5', 4, 3), ('6', 4, 4), ('*', 4, 5, 'special'),
            ('mod', 5, 0), ('ln', 5, 1), ('7', 5, 2), ('8', 5, 3), ('9', 5, 4), ('-', 5, 5, 'special'),
            ('sqrt', 6, 0), ('log', 6, 1), ('.', 6, 2), ('0', 6, 3), ('=', 6, 4), ('+', 6, 5, 'special'),
            ('Delete history', 10, 5),
            ('About app', 11, 5),
        ]

        for (text, row, col, *optional) in buttons:
            btn = ctk.CTkButton(self, text=text, border_width=2, command=lambda t=text: self.on_button_click(t),
                                text_color='#343230', hover_color='#454545')  # hover_color='#7D77DF'
            if optional and optional[0] == 'special':
                btn.configure(fg_color=self.get_code_main_color(self.main_color))
            else:
                btn.configure(fg_color='#f5f5f5')
            btn.grid(row=row, column=col, columnspan=1)
            self.buttons.append(btn)

    def init_history(self):
        self.history_menu = ctk.CTkOptionMenu(self, command=self.history_menu_callback,
                                              fg_color=self.get_code_main_color(self.main_color),
                                              button_color=self.get_code_main_color(self.main_color),
                                              button_hover_color='#454545', text_color='#343230')
        self.history_menu.grid(row=9, column=3, columnspan=3)
        # history =

    def set_history(self, history: list):
        if history:
            tmp = history[0]
            self.optionmenu.configure(values=history)
            self.optionmenu.set(history[0])
            # self.optionmenu.configure(variable=tmp)
            # self.main_buttons.set_history(history)
        else:
            self.optionmenu.set('Empty')
            self.optionmenu.configure(values=history)

    def history_menu_callback(self, choice):
        if choice:  # проверить что если choise нет то все работает
            history_item = choice.rstrip()
            split_lines: list = history_item.split('=')
            self.expression_var.set(split_lines[0])
            self.x_var.set(split_lines[2])

    def init_label(self):
        labels_info = [("Color", 9, 0), ("Background", 10, 0), ("Font size", 11, 0), ("x_min", 7, 0),
                       ("x_max", 7, 3), ("y_min", 8, 0), ("y_max", 8, 3)]
        for label_text, row, column in labels_info:
            label = ctk.CTkLabel(self, text=label_text, text_color='#343230')
            label.grid(row=row, column=column, columnspan=1)

    def on_button_click(self, button_text):
        if button_text == "GRAPH":
            self.graph_button_callback()
        elif button_text == "AC":
            self.expression_var.set('')
        elif button_text == "=":
            if str(self.x_var.get()) != '':
                self.presenter.handle_expression_result(self.expression_var.get(), str(self.x_var.get()))
            else:
                print('ggg')  #
                pass  #
        elif button_text == "Delete history":
            self.presenter.handle_delete_history()
        elif button_text == "About app":
            pass  # справка
        else:
            self.append_to_expression(button_text)

    def graph_button_callback(self) -> None:
        if self.check_coordinates():
            self.presenter.handle_graphic_result(self.expression_var.get(), self.x_min_var.get(), self.x_max_var.get())
        else:
            print('error')
            pass  # error

    def check_coordinates(self) -> bool:
        if (self.x_min_var.get() != '' and self.x_max_var.get() != '' and
                self.y_min_var.get() != '' and self.y_max_var.get() != ''):
            if (float(self.x_min_var.get()) < float(self.x_max_var.get()) and float(self.y_min_var.get()) < float(
                    self.y_max_var.get())):
                return True
        return False

    def add_graph(self, result: list):
        fig, ax = plt.subplots(facecolor=self.get_code_bg_color(self.background))
        plt.scatter(result[0], result[1], marker='.', color=self.get_code_main_color(self.main_color), linewidth=2)
        plt.ylim(float(self.y_min_var.get()), float(self.y_max_var.get()))
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_title(self.expression_var.get())
        plt.grid(True)
        plt.show()

    def set_expression_result(self, res: str) -> None:
        self.expression_var.set(res)

    def append_to_expression(self, text):
        current_expression = self.expression_var.get()
        new_expression = current_expression + text
        self.expression_var.set(new_expression)

    def configure_children(self):
        for child in self.winfo_children():
            child.grid_configure(padx=2, pady=2, sticky="nsew")
