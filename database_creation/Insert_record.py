"""
Created by Mel Davies on 11/05/2022
PROGRAMMING LANGUAGE: Python 3
SCRIPT NAME:insert_record
VERSION = 1.0
SCRIPT STATUS = Working
SCRIPT PURPOSE: Insert a single record into standard_woodscrews
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

onerecord = "INSERT INTO standard_woodscrews(imperial_gauge, metric_gauge, " \
            "head_dia, countersink_drill, shank_dia, shank_clearance_drill, " \
            "softwood_pilot_dia, hardwood_pilot_dia, plug_size, " \
            "masonry_drill) VALUES (%s, %s, %s, %s, %s, %s, %s, " \
            "%s, %s, %s)"

record1 = (2, 2, 4.36, 6.0, 2.38, 2.5, 1.5, 1.5, "None", 0)

my_cursor.execute(onerecord, record1)
mydb.commit()
