"""
Created by Mel Davies on 13/05/2022
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
This works
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Melsic1710@#",
    database="dims",
)

my_cursor = mydb.cursor()

query = "ALTER TABLE standard_woodscrews ADD drive_type INT"
my_cursor.execute(query)
mydb.commit()
