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


# def insert_dept_emp(dept_no, emp_no, from_date=datetime.now().date(), to_date=date(9999, 1, 1)):
#     cnx = connect_default()
#     cursor = cnx.cursor()
#
#     add_salary = ("INSERT INTO dept_emp "
#                   "(dept_no, emp_no, from_date, to_date) "
#                   "VALUES (%(dept_no)s, %(emp_no)s, %(from_date)s, %(to_date)s)")
#
#     # Insert salary information
#     data_salary = {
#         'dept_no': dept_no,
#         'emp_no': emp_no,
#         'from_date': from_date,
#         'to_date': to_date,
#     }
#     cursor.execute(add_salary, data_salary)
#
#     # Make sure data is committed to the database
#     cnx.commit()
#
#     cursor.close()
#     cnx.close()

def insert_location(street, postal_code, city, state):
    cnx = connect_default()
    cursor = cnx.cursor()

    add_salary = ("INSERT INTO locations "
                  "(street_address, postal_code, city, state_province) "
                  "VALUES (%(street_address)s, %(postal_code)s, %(city)s, %(state_province)s)")

    # Insert salary information
    data_salary = {
        'street_address': street,
        'postal_code': postal_code,
        'city': city,
        'state_province': state
    }
    cursor.execute(add_salary, data_salary)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
    dept_no = cursor.lastrowid
    return dept_no


def insert_departments(dept_no, dept_name, location_id):
    cnx = connect_default()
    cursor = cnx.cursor()

    add_salary = ("INSERT INTO departments "
                  "(dept_no, dept_name, location_id) "
                  "VALUES (%(dept_no)s, %(dept_name)s, %(location_id)s)")

    # Insert salary information
    data_salary = {
        'dept_no': dept_no,
        'dept_name': dept_name,
        'location_id': location_id
    }
    cursor.execute(add_salary, data_salary)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
    dept_no = cursor.lastrowid
    return dept_no


def insert_dept_emp(emp_no, dept_no, from_date=datetime.now().date(), to_date=date(9999, 1, 1)):
    cnx = connect_default()
    cursor = cnx.cursor()

    add_dept_emp = ("INSERT INTO dept_emp "
                    "(emp_no, dept_no, from_date, to_date) "
                    "VALUES (%(emp_no)s, %(dept_no)s, %(from_date)s, %(to_date)s)")

    # Insert salary information
    data = {
        'emp_no': emp_no,
        'dept_no': dept_no,
        'from_date': from_date,
        'to_date': to_date,
    }
    cursor.execute(add_dept_emp, data)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


def insert_title(emp_no, title, from_date=datetime.now().date(), to_date=date(9999, 1, 1)):
    cnx = connect_default()
    cursor = cnx.cursor()

    add_salary = ("INSERT INTO titles "
                  "(emp_no, title, from_date, to_date) "
                  "VALUES (%(emp_no)s, %(title)s, %(from_date)s, %(to_date)s)")

    # Insert salary information
    data_salary = {
        'emp_no': emp_no,
        'title': title,
        'from_date': from_date,
        'to_date': to_date
    }
    cursor.execute(add_salary, data_salary)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
    dept_no = cursor.lastrowid
    return dept_no
