# import os file open.

# import excel module
from tkinter import filedialog

import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Please Select your workbook file")
root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))


greeting.pack()

window.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
