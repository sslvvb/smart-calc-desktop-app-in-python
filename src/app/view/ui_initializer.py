import customtkinter as ctk

from .utils import *


class UiInitializer(ctk.CTkFrame):
    def __init__(self, view):
        self.view = view

    def init(self):
        self._init_config()
        self._init_entry()
        self._init_buttons()
        self._init_history()
        self._init_label()
        self._configure_children()

    def update_config(self, key: str, value: str):
        if key == 'main_color':
            for btn in self.view.buttons:
                if btn.cget('fg_color') == get_code_main_color(self.view.main_color):
                    btn.configure(fg_color=get_code_main_color(value))
            for radio in self.view.radio_buttons:
                radio.configure(fg_color=get_code_main_color(value))
            self.view.history_menu.configure(fg_color=get_code_main_color(value),
                                             button_color=get_code_main_color(value))
            self.view.main_color = value
        elif key == 'background':
            self.view.configure(fg_color=get_code_bg_color(value))
            self.view.background = value
        elif key == 'font_size':
            self.view.set_font_size(value)  # change me
            self.view.font_size = value

    def _init_config(self):
        self._init_radio_buttons('main_color', ['pink', 'green'], row=9)
        self._init_radio_buttons('background', ['light', 'dark'], row=10)
        self._init_radio_buttons('font_size', ['14', '16'], row=11)

    def _init_radio_buttons(self, key, values, row):
        var = ctk.StringVar(value=getattr(self.view, key))
        for idx, value in enumerate(values, start=1):
            radio = ctk.CTkRadioButton(self.view, text=value,
                                       command=lambda k=key, v=value: self.view.config_event_callback(k, v),
                                       variable=var, value=value, border_color='#343230', hover_color='#343230',
                                       text_color='#343230', fg_color=get_code_main_color(self.view.main_color))
            radio.grid(row=row, column=idx, columnspan=1)
            self.view.radio_buttons.append(radio)

    def _init_entry(self):
        expression_entry = ctk.CTkEntry(self.view, textvariable=self.view.expression_var)
        expression_entry.grid(row=0, column=0, columnspan=6)

        validate_float_command = self.view.register(validate_float_input)

        entry_settings = [
            (self.view.x_var, "1.0", (1, 2, 3)),
            (self.view.x_min_var, "-10.0", (7, 1, 2)),
            (self.view.x_max_var, "10.0", (7, 4, 2)),
            (self.view.y_min_var, "-10.0", (8, 1, 2)),
            (self.view.y_max_var, "10.0", (8, 4, 2))
        ]

        for var, initial_value, grid_params in entry_settings:
            var.set(initial_value)
            entry = ctk.CTkEntry(self.view, textvariable=var, validate="key")
            entry.grid(row=grid_params[0], column=grid_params[1], columnspan=grid_params[2])
            entry.configure(validatecommand=(validate_float_command, '%P'))

    def _init_buttons(self):
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
            btn = ctk.CTkButton(self.view, text=text, border_width=2,
                                command=lambda t=text: self.view.on_button_click(t),
                                text_color='#343230', hover_color='#454545')
            if optional and optional[0] == 'special':
                btn.configure(fg_color=get_code_main_color(self.view.main_color))
            else:
                btn.configure(fg_color='#f5f5f5')
            btn.grid(row=row, column=col, columnspan=1)
            self.view.buttons.append(btn)

    def _init_history(self):
        self.view.history_menu = ctk.CTkOptionMenu(
            self.view,
            command=self.view.history_menu_callback,
            values=self._history_menu_values(),
            fg_color=get_code_main_color(self.view.main_color),
            button_color=get_code_main_color(self.view.main_color),
            button_hover_color='#454545',
            text_color='#343230',
            dynamic_resizing=False
        )
        self.view.history_menu.grid(row=9, column=3, columnspan=3)

    def _history_menu_values(self):
        return self.view.history if self.view.history else ['No History']

    def _init_label(self):
        labels_info = [
            ("Color", 9, 0), ("Background", 10, 0), ("Font size", 11, 0),
            ("x_min", 7, 0), ("x_max", 7, 3), ("y_min", 8, 0), ("y_max", 8, 3)
        ]

        for label_text, row, column in labels_info:
            label = ctk.CTkLabel(self.view, text=label_text, text_color='#343230')
            label.grid(row=row, column=column, columnspan=1)

    def _configure_children(self):
        for child in self.view.winfo_children():
            child.grid_configure(padx=2, pady=2, sticky="nsew")
        self.view.configure(fg_color=get_code_bg_color(self.view.background))
        self.view.set_font_size(self.view.font_size)
