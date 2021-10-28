from __future__ import print_function

from datetime import date, datetime

from connector import connect_default


def insert_employee(first_name, last_name, gender, birth_date=date(1977, 6, 14), hire_date=datetime.now().date()):
    cnx = connect_default()
    cursor = cnx.cursor()

    add_employee = ("INSERT INTO employees "
                    "(first_name, last_name, hire_date, gender, birth_date) "
                    "VALUES (%s, %s, %s, %s, %s)")
    data_employee = (first_name, last_name, hire_date, gender, birth_date)
    # Insert new employee
    cursor.execute(add_employee, data_employee)
    emp_no = cursor.lastrowid

    cnx.commit()

    cursor.close()
    cnx.close()

    return emp_no


def insert_salary(emp_no, salary, from_date=datetime.now().date(), to_date=date(9999, 1, 1)):
    cnx = connect_default()
    cursor = cnx.cursor()

    add_salary = ("INSERT INTO salaries "
                  "(emp_no, salary, from_date, to_date) "
                  "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

    # Insert salary information
    data_salary = {
        'emp_no': emp_no,
        'salary': salary,
        'from_date': from_date,
        'to_date': to_date,
    }
    cursor.execute(add_salary, data_salary)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
