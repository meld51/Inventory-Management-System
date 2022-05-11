"""
Created by Mel Davies on 11/05/2022
PROGRAMMING LANGUAGE: Python 3
SCRIPT NAME:
VERSION = 0.0
SCRIPT STATUS = Working
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

many_records = "INSERT INTO standard_woodscrews(imperial_gauge, metric_gauge, " \
            "head_dia, countersink_drill, shank_dia, shank_clearance_drill, " \
            "softwood_pilot_dia, hardwood_pilot_dia, plug_size, " \
            "masonry_drill) VALUES (%s, %s, %s, %s, %s, %s, %s, " \
            "%s, %s, %s)"

records = [
    (3, 2.5, 5.16, 6.0, 2.77, 3.0, 1.5, 1.5, "Yellow", 5),
    (4, 3, 5.95, 6.0, 2.77, 3.0, 1.5, 2.0, "Yellow", 5),
    (6,	3.5, 7.14, 8.0,	3.57, 4.0, 2.0,	2.5, "Red",	6),
    (8,	4, 8.73, 9.0, 3.97,	4.5, 2.5, 3.0, "Red/Brown",	7),
    (10, 5,	9.92, 10.0,	4.76, 5.5, 3.0,	3.0, "Brown", 7),
    (12, 5.5, 11.11, 11.0, 5.55, 6.5, 3.0, 3.5,	"Brown", 7),
    (14, 6.5, 12.70, 12.0, 6.35, 7.0, 3.5, 4.0,	"Blue",	10)
]

my_cursor.executemany(many_records, records)
mydb.commit()
