import tkinter as tk

# FOND
LARGE_FOND_STYLE = ("Arial", 25, "bold")
SMALL_FOND_STYLE = ("Arial", 16)
DIGIT_FOND_STYLE = ("Arial", 24, "bold")
DELETE_FOND_STYLE = ("Arial", 15, "bold")

# COLOR
BLACK = "#161621"
WHITE = "#FFFFFF"
RED = "#F94040"
BLUE = "#3498DB"


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.iconbitmap("./calculator photo.ico")
        self.window.geometry("375x587")
        self.window.resizable(0, 0)
        self.window.configure(bg=BLUE)

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        self.total_label, self.label = self.create_display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            ".": (4, 1)
        }
        self.create_digit_button()

        self.operations = {"*": "\u00d7", "-": "-", "+": "+", "/": "\u00f7"}
        self.create_operator_button()

        self.create_clear_button()
        self.create_delete_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.bind_key()

        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.columnconfigure(x, weight=1)
            self.button_frame.rowconfigure(x, weight=1)

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=316, bg=BLUE)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame1 = tk.Frame(self.window, cursor="hand2", bg=WHITE)
        frame1.pack(expand=True, fill="both")
        return frame1

    # ----------------------------------------------------------------------------------------

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=BLUE,
                               fg=WHITE, padx=24, font=SMALL_FOND_STYLE)
        total_label.pack(expand=True, fill="both")
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=BLUE, fg=WHITE, padx=24, font=LARGE_FOND_STYLE)
        label.pack(expand=True, fill="both")
        return total_label, label

    # ------------------------------------------------------------------------------------------

    def create_digit_button(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=BLACK, font=DIGIT_FOND_STYLE,
                               borderwidth=0, command=lambda x=digit: self.digit_button_click(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=2, pady=2)

        button = tk.Button(self.button_frame, text="0", bg=WHITE, fg=BLACK, font=DIGIT_FOND_STYLE,
                           borderwidth=0, command=lambda x=0: self.digit_button_click(x))
        button.grid(row=4, column=2, sticky=tk.NSEW, padx=2, pady=2)

    # ----------------------------------------------------------------------------------------------

    def create_operator_button(self):
        i = 1
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=str(symbol), bg=WHITE, fg=BLUE, font=DIGIT_FOND_STYLE,
                               activeforeground=RED, borderwidth=0,
                               command=lambda x=operator: self.operator_button_click(x))
            button.grid(row=i, column=4, sticky=tk.NSEW, padx=2, pady=2)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=WHITE, fg=RED, font=DIGIT_FOND_STYLE,
                           activeforeground=RED, command=self.clear, borderwidth=0)
        button.grid(row=0, column=2, sticky=tk.NSEW, padx=2, pady=2)

    def create_delete_button(self):
        button = tk.Button(self.button_frame, text="\u232b", bg=WHITE, fg=RED, font=DELETE_FOND_STYLE,
                           activeforeground=RED, borderwidth=0, command=self.delete)
        button.grid(row=0, column=1, sticky=tk.NSEW, padx=2, pady=2)

    def create_equal_button(self):
        button = tk.Button(self.button_frame, text="=", bg=BLUE, fg=WHITE, font=DELETE_FOND_STYLE,
                           activebackground=BLUE, activeforeground=RED, command=self.evaluate, borderwidth=0)
        button.grid(row=4, column=3, sticky=tk.NSEW, padx=2, pady=2)

    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2", bg=WHITE, fg=BLUE, font=DELETE_FOND_STYLE,
                           command=self.square, borderwidth=0)
        button.grid(row=0, column=3, sticky=tk.NSEW, padx=2, pady=2)

    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax", bg=WHITE, fg=BLUE, font=DELETE_FOND_STYLE,
                           command=self.sqrt, borderwidth=0)
        button.grid(row=0, column=4, sticky=tk.NSEW, padx=2, pady=2)

        # ----------------------------------------------------------------------------------------

    def digit_button_click(self, value):
        self.current_expression += str(value)
        self.update_label()

    def operator_button_click(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    # --------------------------------------------------------------------------------------------

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()

    def delete(self):
        self.current_expression = self.current_expression[0:len(self.current_expression) - 1]
        self.update_label()

    def square(self):
        self.current_expression = str(eval(f'{self.current_expression}**2'))
        self.update_label()

    def sqrt(self):
        self.current_expression = str(eval(f'{self.current_expression}**0.5'))
        self.update_label()

    # ----------------------------------------------------------------------------------------------

    def bind_key(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.digit_button_click(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.operator_button_click(operator))
        self.window.bind(key, lambda event, clear=key: self.clear(clear))

    # ------------------------------------------------------------------------------------------------

    def evaluate(self):

        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""

        except Exception as e:
            self.current_expression = "Error"

        finally:
            self.update_label()

    # ------------------------------------------------------------------------------------------------

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbols in self.operations.items():
            expression = expression.replace(operator, f'{symbols}')
        self.total_label.configure(text=expression)

    def update_label(self):
        self.label.configure(text=self.current_expression[:15])

    def run(self):
        self.window.mainloop()


# -------------------------------------------------------------------------------------------

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
