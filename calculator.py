import tkinter as tk

class calculator:

      def __init__(self):
          self.wintdow = tk.Tk()
          self.wintdow.title("Calculetor")
          self.wintdow.iconbitmap("./calculator photo.ico")
          self.wintdow.geometry("355x555")
          self.wintdow.resizable(0,0)



      def run(self):
          self.wintdow.mainloop()


if __name__ == "__main__":
    calc = calculator()
    calc.run()
