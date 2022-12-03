import tkinter as tk

LARGE_FOND_STYLE = ("Arial", 40, "bold")
SMALL_FOND_STYLE = ("Arial", 16)
DIGIT_FOND_STYLE = ("Arial", 24, "bold")

WHITE = "#FFFFFA"
LABEL_COLOR = "#000000"
LIGHT_GRAY = "#F5F5F5"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculetor")
        self.window.iconbitmap("./calculator photo.ico")
        self.window.geometry("375x587")
        self.window.resizable(0, 0)

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
        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=316)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame1 = tk.Frame(self.window, cursor="hand2")
        frame1.pack(expand=True, fill="both")
        return frame1

    # ----------------------------------------------------------------------------------------

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FOND_STYLE)
        total_label.pack(expand=True, fill="both")
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FOND_STYLE)
        label.pack(expand=True, fill="both")
        return total_label, label

    # ------------------------------------------------------------------------------------------

    def create_digit_button(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FOND_STYLE)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=4, pady=4)

        button = tk.Button(self.button_frame, text="0", bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FOND_STYLE)
        button.grid(row=4, column=1, columnspan=2, sticky=tk.NSEW, padx=4, pady=4)

    # ----------------------------------------------------------------------------------------------

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
