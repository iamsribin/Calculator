import tkinter as tk


LARGE_FOND_STYLE = ("Arial", 40, "bold")
SMALL_FOND_STYLE = ("Arial", 16)

LABEL_COLOR = "#8B8B83"
LIGHT_GRAY = "#F5F5F5"

class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculetor")
        self.window.iconbitmap("./calculator photo.ico")
        self.window.geometry("355x555")
        self.window.resizable(0, 0)

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.total_label, self.label = self.create_display_label()
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=226, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_label(self):
         total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                           fg=LABEL_COLOR, padx=24, font=SMALL_FOND_STYLE)
         total_label.pack(expand=True, fill="both")
         label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                     bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FOND_STYLE)
         label.pack(expand=True, fill="both")
         return total_label, label

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
