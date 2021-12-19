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

root.geometry("950x950")
root.title("Inventory Management System")

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()  # column=0 row=0 by default

my_menu = tk.Menu(root)
root.config(menu=my_menu)
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=quit)

welcome_label = ttk.Label(main, text="Welcome to DIMS!",background="#65c09b",
                  foreground="white")
welcome_label.config(font=("Segoe UI", 20))
welcome_label.pack(ipadx=10, ipady=10)

login_label = ttk.Label(main, text="Login Screen", background="#65c09b",
                  foreground="white")
login_label.config(font=("Segoe UI", 15))  # Could be in the constructor
# instead.
login_label.pack(ipadx=10, ipady=10)

username_label = ttk.Label(main, text="Username: ", padding=20)
username_label.config(font=("Segoe UI", 10))
username_label.pack(side="left", padx=5)

username_text = ttk.Entry(main, width=10)
username_text.pack(side="left", padx=5)
username_text.focus()

password_label = ttk.Label(main, text="Password: ", padding=20)
password_label.config(font=("Segoe UI", 10))  # Could be in the constructor instead.
password_label.pack(side="left", padx=5)

password_text = ttk.Entry(main, width=10)
password_text.pack(side="left", padx=5)

temporary_button = ttk.Button(main, text="Move On")
temporary_button.pack(side="right", padx=50)

quit_button = ttk.Button(main, text="Quit", command=root.destroy)
quit_button.pack(side="right", padx=50)

root.mainloop()
