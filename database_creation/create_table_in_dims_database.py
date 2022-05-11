"""
Created by Mel Davies on 11/05/2022
PROGRAMMING LANGUAGE: Python 3
SCRIPT NAME: create_table_in_dims database
VERSION = 1.0
SCRIPT STATUS = Working
SCRIPT PURPOSE: Create standard woodscrew table
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
1. Imports mysqi.connector
2. Connects to correct databas (dims)
3. Connects cursor
4. Constructs empty table with correct columns
5. Lists all the tables in the dims database
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Melsic1710@#",
    database="dims",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE standard_woodscrews"
                  "(woodscrew_id INTEGER AUTO_INCREMENT PRIMARY KEY,"
                  "imperial_gauge INTEGER(4),"
                  "metric_gauge DECIMAL(3,2),"
                  "head_dia DECIMAL(4,2),"
                  "countersink_drill DECIMAL(3,1),"
                  "shank_dia DECIMAL(3,2),"
                  "shank_clearance_drill DECIMAL(2,1),"
                  "softwood_pilot_dia DECIMAL(2,1),"
                  "hardwood_pilot_dia DECIMAL(2,1),"
                  "plug_size VARCHAR(255),"
                  "masonry_drill VARCHAR(255),"
                  "slot_type VARCHAR(255))"
                  )

my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])
