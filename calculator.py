import tkinter as tk

# FOND
LARGE_FOND_STYLE = ("Arial", 40, "bold")
SMALL_FOND_STYLE = ("Arial", 16)
DIGIT_FOND_STYLE = ("Arial", 24, "bold")
DELETE_FOND_STYLE = ("Arial", 15, "bold")

# COLOR
BLACK = "#161621"
WHITE = "#FFFFFF"
RED = "#F94040"
BLUE = "#20459B"


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.iconbitmap("./calculator photo.ico")
        self.window.geometry("375x587")
        self.window.resizable(0, 0)
        self.window.attributes("-alpha", 0.8)
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

        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.columnconfigure(x, weight=1)
            self.button_frame.rowconfigure(x, weight=1)

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=316, bg=BLUE)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame1 = tk.Frame(self.window, cursor="hand2", bg=BLUE)
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
            button = tk.Button(self.button_frame, text=str(digit), bg=BLACK, fg=WHITE, font=DIGIT_FOND_STYLE,
                               activebackground=BLACK, command=lambda x=digit: self.digit_button_click(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=2, pady=2)

        button = tk.Button(self.button_frame, text="0", bg=BLACK, fg=WHITE, font=DIGIT_FOND_STYLE,
                           activebackground=BLACK, command=lambda x=0: self.digit_button_click(x))
        button.grid(row=4, column=2, sticky=tk.NSEW, padx=2, pady=2)

    # ----------------------------------------------------------------------------------------------

    def create_operator_button(self):
        i = 1
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=str(symbol), bg=BLACK, fg=WHITE, font=DIGIT_FOND_STYLE,
                               activeforeground=RED, activebackground=BLACK,
                               command=lambda x=operator: self.operator_button_click(x))
            button.grid(row=i, column=4, sticky=tk.NSEW, padx=2, pady=2)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=RED, fg=BLACK, font=DIGIT_FOND_STYLE,
                           activebackground=RED, activeforeground=WHITE, command=self.clear)
        button.grid(row=0, column=2, sticky=tk.NSEW, padx=2, pady=2)

    def create_delete_button(self):
        button = tk.Button(self.button_frame, text="\u232b", bg=RED, fg=BLACK, font=DELETE_FOND_STYLE,
                           activebackground=RED, activeforeground=WHITE, command=self.delete)
        button.grid(row=0, column=1, sticky=tk.NSEW, padx=2, pady=2)

    def create_equal_button(self):
        button = tk.Button(self.button_frame, text="=", bg=BLACK, fg=WHITE, font=DELETE_FOND_STYLE,
                           activebackground=RED, activeforeground=BLACK, command=self.evaluate)
        button.grid(row=4, column=3, sticky=tk.NSEW, padx=2, pady=2)

    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2", bg=BLACK, fg=WHITE, font=DELETE_FOND_STYLE,
                           command=self.square)
        button.grid(row=0, column=3, sticky=tk.NSEW, padx=2, pady=2)

    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax", bg=BLACK, fg=WHITE, font=DELETE_FOND_STYLE,
                           command=self.sqrt)
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

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(self.total_expression))
        self.total_expression = ""
        self.update_label()

    def update_total_label(self):
        self.total_label.configure(text=self.total_expression)

    # ------------------------------------------------------------------------------------------------

    def update_label(self):
        self.label.configure(text=self.current_expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
