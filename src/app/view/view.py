import customtkinter


class MainButtons(customtkinter.CTkFrame):
    """Custom frame containing checkbox elements for the calculator."""

    def __init__(self, master):
        super().__init__(master)
        self.create_ui()

    def create_ui(self):
        self.expression_entry = customtkinter.CTkEntry(
            self, placeholder_text="Enter an expression", font=("Helvetica", 15))
        self.expression_entry.grid(
            row=0, column=0, columnspan=6, padx=2, pady=(2, 0), sticky="ew")

        self.x_var = customtkinter.StringVar()
        self.x_var.set("1.0")

        self.x_input = customtkinter.CTkEntry(
            self, textvariable=self.x_var, font=("Helvetica", 15))
        self.x_input.grid(
            row=1, column=2, columnspan=3, padx=2, pady=(2, 0), sticky="ew")

        buttons = [
            ('GRAPH', 1, 0), ('x', 1, 1), ('AC', 1, 5),
            ('sin', 2, 0), ('asin', 2, 1), ('e', 2,
                                            2), ('(', 2, 3), (')', 2, 4), ('^', 2, 5),
            ('cos', 3, 0), ('acos', 3, 1), ('1', 3,
                                            2), ('2', 3, 3), ('3', 3, 4), ('/', 3, 5),
            ('tan', 4, 0), ('atan', 4, 1), ('4', 4,
                                            2), ('5', 4, 3), ('6', 4, 4), ('*', 4, 5),
            ('mod', 5, 0), ('ln', 5, 1), ('7', 5,
                                          2), ('8', 5, 3), ('9', 5, 4), ('-', 5, 5),
            ('sqrt', 6, 0), ('log', 6, 1), ('.', 6,
                                            2), ('0', 6, 3), ('=', 6, 4), ('+', 6, 5),
            ('x_min', 7, 0), ('x_max', 7, 3),
            ('y_min', 8, 0), ('y_max', 8, 3),
        ]

        for (text, row, col) in buttons:
            btn = customtkinter.CTkButton(self, text=text, font=("Helvetica", 15),
                                          command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=1,
                     padx=2, pady=2, sticky="ew")

        self.x_min_var = customtkinter.StringVar()
        self.x_min_var.set("1.0")
        self.x_min_input = customtkinter.CTkEntry(
            self, textvariable=self.x_min_var, font=("Helvetica", 15))
        self.x_min_input.grid(
            row=7, column=1, columnspan=2, padx=2, pady=(2, 0), sticky="ew")

        self.x_max_var = customtkinter.StringVar()
        self.x_max_var.set("1.0")
        self.x_max_input = customtkinter.CTkEntry(
            self, textvariable=self.x_max_var, font=("Helvetica", 15))
        self.x_max_input.grid(
            row=7, column=4, columnspan=2, padx=2, pady=(2, 0), sticky="ew")

        self.y_min_var = customtkinter.StringVar()
        self.y_min_var.set("1.0")
        self.y_min_input = customtkinter.CTkEntry(
            self, textvariable=self.y_min_var, font=("Helvetica", 15))
        self.y_min_input.grid(
            row=8, column=1, columnspan=2, padx=2, pady=(2, 0), sticky="ew")

        self.y_max_var = customtkinter.StringVar()
        self.y_max_var.set("1.0")
        self.y_max_input = customtkinter.CTkEntry(
            self, textvariable=self.y_max_var, font=("Helvetica", 15))
        self.y_max_input.grid(
            row=8, column=4, columnspan=2, padx=2, pady=(2, 0), sticky="ew")

    def on_button_click(self):
        print("button pressed")

    def button_callback(self):
        print("button pressed")

    def graph_button_callback(self):
        print("button pressed")


class View(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Calculator")
        self.geometry("1300x700")

        self.main_buttons = MainButtons(self)
        self.main_buttons.grid(row=0, column=0, sticky="nsw")

    # def button_callback(self):
    #     print("button pressed")
