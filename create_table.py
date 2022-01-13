"""
Created by Mel Davies on 13/01/2022
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
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Melsic1710@#",
    database = "dims",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE locations (primary_location VARCHAR(255),"
                  "secondary_location VARCHAR (255),"
                  "tertiary_location VARCHAR (255), location_id INTEGER "
                  "AUTO_INCREMENT PRIMARY "
                  "KEY)")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])
