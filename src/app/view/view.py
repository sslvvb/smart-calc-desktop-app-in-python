import customtkinter

from .graphic import Graphic
from presenter import presenter


class View(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Calculator")
        self.geometry("865x390")
        self.presenter = None
        self.expression_var = None
        self.expression_entry = None
        self.x_var = None
        self.x_input = None
        self.x_min_var = None
        self.x_min_input = None
        self.x_max_var = None
        self.x_max_input = None
        self.y_min_var = None
        self.y_min_input = None
        self.y_max_var = None
        self.y_max_input = None
        self.optionmenu = None
        self.radiobutton_1 = None
        self.radiobutton_2 = None
        self.toplevel_window = None

    def init_ui(self, presenter: presenter.Presenter) -> None:
        self.presenter = presenter
        # Устанавливаем распределение строк и столбцов для центрирования
        self.grid_rowconfigure(0, weight=1)  # Распределение по вертикали
        self.grid_columnconfigure(0, weight=1)  # Распределение по горизонтали

        self.init_entry()
        self.init_buttons()
        self.init_history()
        self.init_config()

    def init_entry(self):
        self.expression_var = customtkinter.StringVar()
        self.expression_entry = customtkinter.CTkEntry(self, font=("Helvetica", 15), textvariable=self.expression_var)
        self.expression_entry.grid(row=0, column=0, columnspan=6, padx=2, pady=(2, 0), sticky="nsew")

        self.x_var = customtkinter.StringVar()
        self.x_var.set("1.0")
        self.x_input = customtkinter.CTkEntry(self, textvariable=self.x_var, font=("Helvetica", 15))
        self.x_input.grid(row=1, column=2, columnspan=3, padx=2, pady=(2, 0), sticky="nsew")

        self.x_min_var = customtkinter.StringVar()
        self.x_min_var.set("1.0")
        self.x_min_input = customtkinter.CTkEntry(self, textvariable=self.x_min_var, font=("Helvetica", 15))
        self.x_min_input.grid(row=7, column=1, columnspan=2, padx=2, pady=(2, 0), sticky="nsew")

        self.x_max_var = customtkinter.StringVar()
        self.x_max_var.set("1.0")
        self.x_max_input = customtkinter.CTkEntry(self, textvariable=self.x_max_var, font=("Helvetica", 15))
        self.x_max_input.grid(row=7, column=4, columnspan=2, padx=2, pady=(2, 0), sticky="nsew")

        self.y_min_var = customtkinter.StringVar()
        self.y_min_var.set("1.0")
        self.y_min_input = customtkinter.CTkEntry(self, textvariable=self.y_min_var, font=("Helvetica", 15))
        self.y_min_input.grid(row=8, column=1, columnspan=2, padx=2, pady=(2, 0), sticky="nsew")

        self.y_max_var = customtkinter.StringVar()
        self.y_max_var.set("1.0")
        self.y_max_input = customtkinter.CTkEntry(self, textvariable=self.y_max_var, font=("Helvetica", 15))
        self.y_max_input.grid(row=8, column=4, columnspan=2, padx=2, pady=(2, 0), sticky="nsew")

    def init_buttons(self):
        buttons = [
            ('GRAPH', 1, 0), ('x', 1, 1), ('AC', 1, 5),
            ('sin', 2, 0), ('asin', 2, 1), ('e', 2, 2), ('(', 2, 3), (')', 2, 4), ('^', 2, 5),
            ('cos', 3, 0), ('acos', 3, 1), ('1', 3, 2), ('2', 3, 3), ('3', 3, 4), ('/', 3, 5),
            ('tan', 4, 0), ('atan', 4, 1), ('4', 4, 2), ('5', 4, 3), ('6', 4, 4), ('*', 4, 5),
            ('mod', 5, 0), ('ln', 5, 1), ('7', 5, 2), ('8', 5, 3), ('9', 5, 4), ('-', 5, 5),
            ('sqrt', 6, 0), ('log', 6, 1), ('.', 6, 2), ('0', 6, 3), ('=', 6, 4), ('+', 6, 5),
            ('x_min', 7, 0), ('x_max', 7, 3),
            ('y_min', 8, 0), ('y_max', 8, 3),
            ('Delete history', 10, 5),
        ]

        for (text, row, col) in buttons:
            if text == 'x_min' or text == 'x_max' or text == 'y_min' or text == 'y_max':
                btn = customtkinter.CTkButton(self, text=text, font=("Helvetica", 15), state='disabled',
                                              command=lambda t=text: self.on_button_click(t))
            else:
                btn = customtkinter.CTkButton(self, text=text, font=("Helvetica", 15),
                                              command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=1, padx=2, pady=2, sticky="nsew")

    def init_history(self):
        # history =
        self.optionmenu = customtkinter.CTkOptionMenu(self, command=self.history_menu_callback)
        self.optionmenu.grid(row=9, column=3, columnspan=3, padx=2, pady=2, sticky="nsew")

    def init_config(self):
        def radiobutton_event():
            print("radiobutton toggled, current value:", bg_var.get())

        bg_var = customtkinter.IntVar(value=2)
        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="PINK", command=radiobutton_event,
                                                          variable=bg_var, value=1)
        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="GREEN", command=radiobutton_event,
                                                          variable=bg_var, value=2)
        self.radiobutton_1.grid(row=9, column=1, columnspan=1, padx=2, pady=2, sticky="nsew")
        self.radiobutton_2.grid(row=9, column=2, columnspan=1, padx=2, pady=2, sticky="nsew")

        label = customtkinter.CTkLabel(self, text="Select main color", corner_radius=4,
                                       fg_color=['yellow', 'black'])
        label.grid(row=9, column=0, columnspan=1, padx=2, pady=2, sticky="nsew")
        label = customtkinter.CTkLabel(self, text="Select background color", corner_radius=4,
                                       fg_color=['yellow', 'black'])
        label.grid(row=10, column=0, columnspan=1, padx=2, pady=2, sticky="nsew")
        label = customtkinter.CTkLabel(self, text="Select font size", corner_radius=4,
                                       fg_color=['yellow', 'black'])
        label.grid(row=11, column=0, columnspan=1, padx=2, pady=2, sticky="nsew")

    def on_button_click(self, button_text):
        if button_text == "GRAPH":
            self.graph_button_callback()
        elif button_text == "AC":
            self.expression_var.set('')
        elif button_text == "Delete history":
            self.presenter.handle_delete_history()
        elif button_text == "=":
            self.presenter.handle_expression_result(self.expression_var.get(), self.x_var.get())
        else:
            self.append_to_expression(button_text)

    def graph_button_callback(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Graphic(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def set_expression_result(self, res: str) -> None:
        self.expression_var.set(res)

    def append_to_expression(self, text):
        current_expression = self.expression_var.get()
        new_expression = current_expression + text
        self.expression_var.set(new_expression)

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
