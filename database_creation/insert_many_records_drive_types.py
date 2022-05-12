"""
Created by Mel Davies on 12/05/2022
PROGRAMMING LANGUAGE: Python 3
SCRIPT NAME:
VERSION = 0.0
SCRIPT STATUS =
SCRIPT PURPOSE:
TARGET SYSTEM: Windows 10
INTERFACE: Command Line or Pycharm
DEVELOPMENT ENVIRONMENT: Pycharm
NON_FUNCTIONAL REQUIREMENTS:
FUNCTIONAL REQUIREMENTS:
TESTING: 
PyLint:
Unit Test:
REMAINING PROBLEMS
DESCRIPTION OF FUNCTIONALITY
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Melsic1710@#",
    database="dims",
)

my_cursor = mydb.cursor()

many_records = "INSERT INTO drive_types(screwdriver_type, blank) VALUES (%s, " \
               "%s)"

# NOTE: This won't work if each record has a singler input. Don't know why!
records = [
    ("Slotted", "blank"),
    ("Pozidriv", "blank"),
    ("Philips", "blank"),
    ("Torx", "blank")
]

my_cursor.executemany(many_records, records)
mydb.commit()
