import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.ttk import *

window = Tk()
window.title("Guess Who?")
window.state("zoomed")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

mainframe = ttk.Frame(window, padding=(3,3,12,12))
secondframe = ttk.Frame(mainframe, borderwidth=10, relief="ridge", width=1000, height=500)
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
secondframe.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=E)
one = ttk.Label(mainframe, text="One").grid(column=0,row=0)
Two = ttk.Label(secondframe, text="Two").grid(column=0,row=0)

window.mainloop()