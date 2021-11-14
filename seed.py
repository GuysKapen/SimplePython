from datetime import date, datetime

from connector import connect_default
import random

from_date = datetime.now().date()
to_date = date(9999, 1, 1)
cnx = connect_default()
cursor = cnx.cursor()

add_location = ("INSERT INTO locations "
                "(street_address, postal_code, city, state_province) "
                "VALUES (%(street_address)s, %(postal_code)s, %(city)s, %(state_province)s)")

data_location = [
    {
        'street_address': "3048 Upland Avenue",
        'postal_code': "33316",
        'city': "FORT LAUDERDALE",
        'state_province': "Florida"
    },
    {
        'street_address': "1801 Loving Acres Road",
        'postal_code': "76133",
        'city': "Wedgwood",
        'state_province': "Texas"
    },
    {
        'street_address': "3960 Leo Street",
        'postal_code': "80227",
        'city': "Lakewood",
        'state_province': "Colorado"
    },
    {
        'street_address': "1677 Dogwood Lane",
        'postal_code': "85630",
        'city': "Saint David",
        'state_province': "Arizona"
    },
    {
        'street_address': "1239 Pleasant Hill Road",
        'postal_code': "92664",
        'city': "Irvine",
        'state_province': "California"
    },
]

for data in data_location:
    cursor.execute(add_location, data)
cnx.commit()

add_department = ("INSERT INTO departments "
                  "(dept_name, location_id) "
                  "VALUES (%(dept_name)s, %(location_id)s)")

data_department = [
    {
        'dept_name': "Success Is Yours",
        'location_id': 1
    },
    {
        'dept_name': "Strawberries",
        'location_id': 2
    },
    {
        'dept_name': "Sherman's",
        'location_id': 3
    },
    {
        'dept_name': "Grey Fade",
        'location_id': 3
    },
    {
        'dept_name': "Parts and Pieces",
        'location_id': 4
    },
    {
        'dept_name': "Total Yard Management",
        'location_id': 4
    },
]

for data in data_department:
    cursor.execute(add_department, data)
cnx.commit()

add_employee = ("INSERT INTO employees "
                "(first_name, last_name, birth_date, gender, hire_date) "
                "VALUES (%s, %s, %s, %s, %s)")

data_employees = [
    ("Rodolfo J", "McCaskill", date(1977, 6, 14), "M", datetime.now().date()),
    ("Ken E", "Barker", date(1987, 6, 22), "M", datetime.now().date()),
    ("Nathan B", "Keyser", date(1977, 1, 9), "M", datetime.now().date()),
    ("Alison K", "Howell", date(1998, 12, 7), "F", datetime.now().date()),
    ("Marilyn K", "Fraser", date(1993, 8, 7), "F", datetime.now().date()),
    ("Charles S", "Barker", date(1958, 7, 26), "M", datetime.now().date()),
    ("Steven S", "Lyda", date(1968, 4, 15), "M", datetime.now().date()),
    ("Leona A", "Buster", date(1987, 11, 26), "F", datetime.now().date()),
    ("Manuel J", "Nettles", date(1969, 11, 23), "M", datetime.now().date()),
]

for data in data_employees:
    cursor.execute(add_employee, data)
cnx.commit()

add_dept_emp = ("INSERT INTO dept_emp "
                "(emp_no, dept_no, from_date, to_date) "
                "VALUES (%(emp_no)s, %(dept_no)s, %(from_date)s, %(to_date)s)")

emp_no_dept_no = list(set([(i, random.randint(1, 6)) for i in range(1, len(data_employees) + 1)]))

data_dept_emp = [{
    'emp_no': emp_no,
    'dept_no': dept_no,
    'from_date': from_date,
    'to_date': to_date,
} for emp_no, dept_no in emp_no_dept_no]

for data in data_dept_emp:
    cursor.execute(add_dept_emp, data)
cnx.commit()

add_title = ("INSERT INTO titles "
             "(emp_no, title, from_date, to_date) "
             "VALUES (%(emp_no)s, %(title)s, %(from_date)s, %(to_date)s)")

data_title = [
    {
        'emp_no': 1,
        'title': "Nanotechnology Engineering Technician",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 2,
        'title': "Electronic Equipment Installer and Repairer",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 3,
        'title': "Agricultural Worker, All Other",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 4,
        'title': "Surveying Technician",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 5,
        'title': "Urologist",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 6,
        'title': "Chemical Engineer",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 7,
        'title': "Chemical Engineer",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 8,
        'title': "Home Economics Teacher, Postsecondary",
        'from_date': from_date,
        'to_date': to_date
    },
    {
        'emp_no': 9,
        'title': "Coating, Painting, and Spraying Machine Setter",
        'from_date': from_date,
        'to_date': to_date
    },
]

for data in data_title:
    cursor.execute(add_title, data)
cnx.commit()

add_absent = ("INSERT INTO employees_absent "
              "(emp_no, abs_date, has_permission_form, abs_hours) "
              "VALUES (%(emp_no)s, %(abs_date)s, %(has_permission_form)s, %(abs_hours)s)")

data_absent = [{
    'emp_no': random.randint(1, 9),
    'abs_date': date(2021, random.randint(1, 12), random.randint(1, 26)),
    'has_permission_form': random.choice([True, False]),
    'abs_hours': random.randint(1, 8)
} for _ in range(100)]

for data in data_absent:
    cursor.execute(add_absent, data)
cnx.commit()

add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

# Insert salary information
data_salaries = [{
    'emp_no': emp_no,
    'salary': random.randint(32000, 64000),
    'from_date': from_date,
    'to_date': to_date
} for emp_no in range(1, len(data_employees) + 1)]

for data in data_salaries:
    cursor.execute(add_salary, data)
cnx.commit()
