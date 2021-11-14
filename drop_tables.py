import mysql.connector
from mysql.connector import errorcode

from main import connect_default

cnx = connect_default()
cursor = cnx.cursor()

cursor.execute("drop table dept_emp;")
cursor.execute("drop table dept_manager;")
cursor.execute("drop table departments;")
cursor.execute("drop table employees_absent;")
cursor.execute("drop table locations;")
cursor.execute("drop table salaries;")
cursor.execute("drop table titles;")
cursor.execute("drop table employees;")