"""
Created by Mel Davies on 30/12/2021
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
    database = "mels_trial_database",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE users"
                  "(user_id INTEGER(10),"
                  "name VARCHAR(255),"
                  "email VARCHAR(255),"
                  "age INTEGER(10))"
                  )

my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])

