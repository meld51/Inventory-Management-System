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

2. Splash Screen
https://www.tutorialspoint.com/how-to-create-a-splash-screen-using-tkinter

"""

# TODO Give the splash a picture

import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --


def login_window():
    """define login window"""
    login_window = tk.Tk()
    login_window.geometry("240x200")
    login_window.title('Inventory Management System')
    login_window.resizable(0, 0)
    login_window.eval('tk::PlaceWindow . center')

    # configure the grid
    login_window.columnconfigure(0, weight=1)
    login_window.columnconfigure(1, weight=3)

    # Provide a menu
    my_menu = tk.Menu(login_window)
    login_window.config(menu=my_menu)
    file_menu = tk.Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Quit", command=quit)

    # welcome_label = ttk.Label(root, text="Welcome to DIMS!",
    # background="#65c09b",
    #                  foreground="white")
    # welcome_label.config(font=("Segoe UI", 20))
    # welcome_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    # login_label = ttk.Label(root, text="Login Screen", background="#65c09b",
    #                  foreground="white")
    # login_label.grid(column=1, row=0)
    # login_label.config(font=("Segoe UI", 15))

    # username
    username_label = ttk.Label(login_window, text="Username:")
    username_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

    username_entry = ttk.Entry(login_window)
    username_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
    username_entry.focus()

    # password
    password_label = ttk.Label(login_window, text="Password:")
    password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

    password_entry = ttk.Entry(login_window,  show="*")
    password_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

    # login button
    login_button = ttk.Button(login_window, text="Login")
    login_button.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

    quit_button = ttk.Button(login_window, text="Quit", command=login_window.destroy)
    quit_button.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

    temporary_button = ttk.Button(login_window, text="Move On")
    temporary_button.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

    login_window.mainloop()


# Create an instance of tkinter frame
splash_win = tk.Tk()
splash_win.title('Inventory Management System')
splash_win.resizable(0, 0)
MyLeftPos = (splash_win.winfo_screenwidth() - 800) / 2
myTopPos = (splash_win.winfo_screenheight() - 800) / 2
splash_win.geometry("%dx%d+%d+%d" % (800, 800, MyLeftPos, myTopPos))

# Set the title of the window
splash_win.title("Splash")

# Splash Window Timer
splash_win.after(1000, login_window)
splash_win.mainloop()
