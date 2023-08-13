import customtkinter

_HELP_TEXT = """Welcome to SmartCalc 3.0

SmartCalc is a powerful calculator application that allows you to perform a wide range of mathematical operations, visualize functions, and manage your calculation history.

Key Features:
- Advanced Arithmetic: Perform arithmetic operations such as addition, subtraction, multiplication, and division on integers and real numbers. Use parentheses to control the order of operations.
- Fractional Precision: SmartCalc ensures high accuracy in the fractional part of the results.
- History Management: Store and recall your past calculations from the history panel. Load expressions for re-evaluation and clear the entire history as needed.
- Persistent History: Your calculation history is automatically saved between application runs, so you can pick up where you left off.
- Function Plotting: Plot graphs of functions defined by expressions in infix notation with a variable 'x'. Customize the display and range of the graph to suit your needs.

Supported Operations and Functions:
- Basic Arithmetic: + (Addition), - (Subtraction), * (Multiplication), / (Division)
- Exponentiation: ^ (Power)
- Square Root: sqrt(x)
- Trigonometric Functions: sin(x), asin(x), cos(x), acos(x), tan(x), atan(x)
- Logarithmic Functions: log(x), ln(x)
- Parentheses: ( and ) for grouping expressions
- Variable 'x': Use 'x' as a variable in your expressions
- 'e' for exponential form

Using SmartCalc:
1. Enter your expression.
2. Utilize parentheses to group sub-expressions as needed.
3. Press '=' to calculate the result of the expression.
4. Explore the history panel to review past calculations and reload expressions.
5. To plot a function, enter the function expression, specify the display range, and press 'GRAPH'.

Limitations:
- Input can contain up to 255 characters.
- Graphs are limited to the defined value area and definition area.

SmartCalc Version 3.0 | Developed by @sslvvb"""


class About(customtkinter.CTkToplevel):
    def __init__(self, *args, background: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('About')
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = customtkinter.CTkTextbox(master=self, width=500, height=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", _HELP_TEXT)
        self.textbox.configure(fg_color=background)
