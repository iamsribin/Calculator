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
        self.window.title("Calculetor")
        self.window.iconbitmap("./calculator photo.ico")
        self.window.geometry("375x587")
        self.window.resizable(0, 0)
        self.window.attributes("-alpha", 0.8)
        self.window.configure(bg=BLUE)

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        self.total_label, self.label = self.create_display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            ".": (4, 3)
        }
        self.create_digit_button()

        self.operations = {"*": "\u00d7", "-": "-", "+": "+"}
        self.create_operator_button()
        
        self.create_clear_button()
        self.create_delete_button()
        self.create_equal_button()

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
                               activebackground=BLACK,)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=2, pady=2)

        button = tk.Button(self.button_frame, text="0", bg=BLACK, fg=WHITE, font=DIGIT_FOND_STYLE,
                           activebackground=BLACK)
        button.grid(row=4, column=1, columnspan=2, sticky=tk.NSEW, padx=2, pady=2)

    # ----------------------------------------------------------------------------------------------

    def create_operator_button(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=str(symbol), bg=BLACK, fg=WHITE, font=DIGIT_FOND_STYLE,
                               activeforeground=RED, activebackground=BLACK)
            button.grid(row=i, column=4, sticky=tk.NSEW, padx=2, pady=2)
            i += 1

        button = tk.Button(self.button_frame, text="\u00f7", bg=BLACK, fg=WHITE, font=DIGIT_FOND_STYLE,
                           activeforeground=RED, activebackground=BLACK)
        button.grid(row=0, column=3, sticky=tk.NSEW, padx=2, pady=2)

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=RED, fg=BLACK, font=DIGIT_FOND_STYLE,
                           activebackground=RED, activeforeground=WHITE)
        button.grid(row=0, column=2, sticky=tk.NSEW, padx=2, pady=2)

    def create_delete_button(self):
        button = tk.Button(self.button_frame, text="\u232b", bg=RED, fg=BLACK, font=DELETE_FOND_STYLE,
                           activebackground=RED, activeforeground=WHITE)
        button.grid(row=0, column=1, sticky=tk.NSEW, padx=2, pady=2)

    def create_equal_button(self):
        button = tk.Button(self.button_frame, text="=", bg=BLACK, fg=WHITE, font=DELETE_FOND_STYLE,
                           activebackground=RED, activeforeground=BLACK)
        button.grid(row=3, rowspan=4, column=4, sticky=tk.NSEW, padx=2, pady=2)

        # ----------------------------------------------------------------------------------------

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
