import tkinter as tk

LIGHT_GRAY = "#F5F5F5"


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculetor")
        self.window.iconbitmap("./calculator photo.ico")
        self.window.geometry("355x555")
        self.window.resizable(0, 0)

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=226, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
