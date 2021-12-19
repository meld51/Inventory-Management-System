"""
Created by Mel Davies on 17/12/2021
PROGRAMMING LANGUAGE: Python 3
SCRIPT NAME: Domestic Inventory Management System
VERSION = 0.1
SCRIPT STATUS = WIP
SCRIPT PURPOSE:
TARGET SYSTEM: Windows 10
INTERFACE: Command Line or Pycharm
DEVELOPMENT ENVIRONMENT: Pycharm
NON FUNCTIONAL REQUIREMENTS:
FUNCTIONAL REQUIREMENTS:
TESTING:
PyLint:
Unit Test:
REMAINING PROBLEMS
DESCRIPTION OF FUNCTIONALITY


Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
# importing tkinter for gui
# importing tkinter gui
import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

# creating window
root = tk.Tk()

# getting screen width and height of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.title("Inventory Management System")

my_menu = tk.Menu(root)
root.config(menu=my_menu)
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=quit)

label = ttk.Label(root, text="Welcome to DIMS!", padding=20)
label.config(font=("Segoe UI", 20))  # Could be in the constructor instead.
label.pack()

label = ttk.Label(root, text="Login", padding=20)
label.config(font=("Segoe UI", 10))  # Could be in the constructor instead.
label.pack(side="left", padx=50)

label = ttk.Label(root, text="Username: ", padding=20)
label.config(font=("Segoe UI", 10))  # Could be in the constructor instead.
label.pack(side="left", padx=50)

label = ttk.Label(root, text="Password: ", padding=20)
label.config(font=("Segoe UI", 10))  # Could be in the constructor instead.
label.pack(side="left", padx=50)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", padx=50)

root.mainloop()
