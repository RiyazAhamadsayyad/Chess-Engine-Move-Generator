import tkinter as tk

from gui import ChessGUI


if __name__ == "__main__":

    root = tk.Tk()

    app = ChessGUI(root)

    root.mainloop()