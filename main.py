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

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --


def size_window():
    pass


def logout():
    pass

def new_stock_location():
    """When this button is selected the user will be taken to a new window to
    allow for Stock Location Creation"""
    pass

def amend_stock_location():
    """When this button is selected the user will be taken to a new window to
    allow for location amendment"""
    pass

def delete_stock_location():
    """When this button is selected the user will be taken to a new window to
    allow for location deletion"""
    pass


def print_stock_location():
    """prints a single stock Location"""
    pass

def print_all_stock_locations():
    """prints all stock locations"""
    pass

def stock_location():
    stock_location_window = tk.Tk()
    stock_location_window.title("Stock Location Window")

    stock_location_window.resizable(0, 0)
    my_left_pos = (stock_location_window.winfo_screenwidth() - 550) / 2
    my_top_pos = (stock_location_window.winfo_screenheight() - 500) / 2
    stock_location_window.geometry("%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    # Create New Location
    new_location_button = ttk.Button(stock_location_window,
                              text="Create New Location",
                              command=new_stock_location)
    new_location_button.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

    # Amend existing stock location
    amend_location_button = ttk.Button(stock_location_window,
                                     text="Amend Location",
                                     command=amend_stock_location)
    amend_location_button.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

    # Delete Location
    delete_location_button = ttk.Button(stock_location_window,
                                     text="Delete Location",
                                     command=delete_stock_location)
    delete_location_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


    # print a stock location
    print_all_stock_locations_button = ttk.Button(stock_location_window,
                                       text="Print Stock Location",
                                       command=print_stock_location)
    print_all_stock_locations_button.grid(column=1, row=4, sticky=tk.W, padx=5,
                                    pady=5)

    # print all stock locations
    print_location_button = ttk.Button(stock_location_window,
                                       text="Print All Stock Locations",
                                       command=print_all_stock_locations)
    print_location_button.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)


    new_location_button = ttk.Button(stock_location_window,
                                     text="Create New Location",
                                     command=new_stock_location)
    new_location_button.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)



    stock_location_window.mainloop()


def stock_items():
    stock_items_window = tk.Tk()
    stock_items_window.title("Stock Items Window")

    stock_items_window.resizable(0, 0)
    my_left_pos = (stock_items_window.winfo_screenwidth() - 550) / 2
    my_top_pos = (stock_items_window.winfo_screenheight() - 500) / 2
    stock_items_window.geometry(
        "%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    stock_items_window.mainloop()


def stock_finder():
    stock_finder_window = tk.Tk()
    stock_finder_window.title("Stock Finder")

    stock_finder_window.resizable(0, 0)
    my_left_pos = (stock_finder_window.winfo_screenwidth() - 550) / 2
    my_top_pos = (stock_finder_window.winfo_screenheight() - 500) / 2
    stock_finder_window.geometry(
        "%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    stock_finder_window.mainloop()


def stock_counter():
    stock_counter_win = tk.Tk()
    stock_counter_win.title("Stock Counter")

    stock_counter_win.resizable(0, 0)
    my_left_pos = (stock_counter_win.winfo_screenwidth() - 550) / 2
    my_top_pos = (stock_counter_win.winfo_screenheight() - 500) / 2
    stock_counter_win.geometry(
        "%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    stock_counter_win.mainloop()


def stock_sorter():
    stock_sorter_win = tk.Tk()
    stock_sorter_win.title("Stock Sorter")

    stock_sorter_win.resizable(0, 0)
    my_left_pos = (stock_sorter_win.winfo_screenwidth() - 550) / 2
    my_top_pos = (stock_sorter_win.winfo_screenheight() - 500) / 2
    stock_sorter_win.geometry(
        "%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    stock_sorter_win.mainloop()


def shortages():
    shortages_win = tk.Tk()
    shortages_win.title("Shortages")

    shortages_win.resizable(0, 0)
    my_left_pos = (shortages_win.winfo_screenwidth() - 550) / 2
    my_top_pos = (shortages_win.winfo_screenheight() - 500) / 2
    shortages_win.geometry(
        "%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    shortages_win.mainloop()


def orders():
    orders_win = tk.Tk()
    orders_win.title("Orders")

    orders_win.resizable(0, 0)
    my_left_pos = (orders_win.winfo_screenwidth() - 550) / 2
    my_top_pos = (orders_win.winfo_screenheight() - 500) / 2
    orders_win.geometry("%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    orders_win.mainloop()


def choice():
    """Main choices"""
    decision_window = tk.Tk()
    decision_window.title("Decision Window")
    decision_window.resizable(0, 0)
    my_left_pos = (decision_window.winfo_screenwidth() - 550) / 2
    my_top_pos = (decision_window.winfo_screenheight() - 500) / 2
    decision_window.geometry("%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

    info_label = ttk.Label(decision_window, text="Choose an Option",
                           background="#65c09b", foreground="white",
                           font=("Segoe UI", 25))
    info_label.grid(column=1, row=1)

    # stock location button
    login_button = ttk.Button(decision_window,
                              text="Stock Location",
                              command=stock_location)
    login_button.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

    # stock items button
    login_button = ttk.Button(decision_window,
                              text="Stock Items",
                              command=stock_items)
    login_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

    # stock finder button
    login_button = ttk.Button(decision_window,
                              text="Stock Finder",
                              command=stock_finder)
    login_button.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

    # stock counter button
    login_button = ttk.Button(decision_window,
                              text="Stock Counter",
                              command=stock_counter)
    login_button.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

    # stock sorter button
    login_button = ttk.Button(decision_window,
                              text="Stock Sorter",
                              command=stock_sorter)
    login_button.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

    # shortages button
    login_button = ttk.Button(decision_window,
                              text="Shortages",
                              command=shortages)
    login_button.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

    # orders button
    login_button = ttk.Button(decision_window,
                              text="Orders",
                              command=orders)
    login_button.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

    # logout button
    login_button = ttk.Button(decision_window,
                              text="Logout",
                              command=logout)
    login_button.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

    decision_window.mainloop()


def login_window():
    """define login window"""
    splash_win.destroy()
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

    temporary_button = ttk.Button(login_window, text="Move On", command=choice)
    temporary_button.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

    login_window.mainloop()


# Create an instance of tkinter frame
splash_win = tk.Tk()
splash_win.title('Inventory Management System')
splash_win.resizable(0, 0)
my_left_pos = (splash_win.winfo_screenwidth() - 550) / 2
my_top_pos = (splash_win.winfo_screenheight() - 500) / 2
splash_win.geometry("%dx%d+%d+%d" % (550, 500, my_left_pos, my_top_pos))

# Set the title of the window
# splash_win.title("Splash")

welcome_label = ttk.Label(splash_win, text="Welcome to DIMS!",
                          background="#65c09b", foreground="white",
                          font=("Segoe UI", 25)).pack()
# tk.Label(splash_win, text="Label 2", bg="red").pack(side="left")

# Background Image
canvas = tk.Canvas(
        splash_win,
        width=500,
        height=500
        )

canvas.pack()

img = ImageTk.PhotoImage(Image.open('Images/background_1.jpg'))

canvas.create_image(
        10,
        10,
        anchor=NW,
        image=img
)
# Splash Window Timer
splash_win.after(1000, login_window)
splash_win.mainloop()
