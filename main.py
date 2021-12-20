"""
Created by Mel Davies on 20/12/2021
PROGRAMMING LANGUAGE: Python 3
SCRIPT NAME:
VERSION = 0.0
SCRIPT STATUS =
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

WEBSITES
1. Grids
https://www.pythontutorial.net/tkinter/tkinter-grid/
"""
import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

# root window
root = tk.Tk()
root.geometry("240x200")
root.title('Inventory Management System')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Provide a menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=quit)

#welcome_label = ttk.Label(root, text="Welcome to DIMS!",background="#65c09b",
#                  foreground="white")
#welcome_label.config(font=("Segoe UI", 20))
#welcome_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

#login_label = ttk.Label(root, text="Login Screen", background="#65c09b",
#                  foreground="white")
#login_label.grid(column=1, row=0)
#login_label.config(font=("Segoe UI", 15))

# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
username_entry.focus()

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

temporary_button = ttk.Button(root, text="Move On")
temporary_button.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

root.mainloop()
