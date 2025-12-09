
from database import criar_tabela
from interface import App
import tkinter as tk

criar_tabela()

root = tk.Tk()
App(root)
root.mainloop()
