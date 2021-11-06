from connector import connect_default
from insert_data import insert_employee, insert_salary, insert_departments, insert_dept_emp, insert_location, \
    insert_title, insert_absent
from tabulate import tabulate


def input_insert_employee():
    first_name = input('Input first_name of employee: ')
    last_name = input('Input last_name of employee: ')
    gender = input('Input gender of employee (F/M): ')
    if gender != 'M' and gender != 'F':
        print("Invalid gender. Please try again.")
        return
    return insert_employee(first_name, last_name, gender)


def input_insert_salary(emp_no=None):
    if emp_no is None:
        emp_no = input('Input emp_no of employee: ')
    salary = input('Input salary of employee: ')
    insert_salary(emp_no, salary)


def input_insert_location():
    address = input("Input address: ")
    postal_code = input("Input postal_code: ")
    city = input('Input city: ')
    state = input('Input state: ')
    return insert_location(address, postal_code, city, state)


def input_insert_dept():
    dept_no = input("Input dept_no: ")
    dept_name = input("Input dept_name: ")
    location_id = input('Input location_id: ')
    return insert_departments(dept_no, dept_name, location_id)


def input_insert_dept_emp():
    dept_no = input_insert_dept()
    emp_no = input_insert_employee()
    insert_dept_emp(emp_no, dept_no)


def input_insert_employee_and_salary():
    emp_no = input_insert_employee()
    input_insert_salary(emp_no)


def input_insert_title(emp_no=None):
    if emp_no is None:
        emp_no = input("Input emp_no: ")
    title = input("Input title: ")
    insert_title(emp_no, title)


def input_insert_employee_salary_and_title():
    emp_no = input_insert_employee()
    input_insert_salary(emp_no)
    input_insert_title(emp_no)


def execute_procedure_list_all_employees():
    """
    Execute procedure list_all_employees
    delimiter //
    CREATE PROCEDURE list_all_employees()
    BEGIN
        SELECT * FROM employees;
    END//
    delimiter;
    :return: 
    """
    cnx = connect_default()
    cursor = cnx.cursor()

    cursor.execute("call list_all_employees()")
    results = cursor.fetchall()
    print(tabulate(results, headers=['ID', 'DOB', 'First Name', 'Last Name', 'Gender', 'Hire Date']))


def execute_procedure_list_all_employees_with_salary():
    """
    Execute procedure list_all_employees_with_salary
    drop procedure list_all_employees_with_salary;
    delimiter //
    CREATE PROCEDURE list_all_employees_with_salary()
    BEGIN
        SELECT e.*, s.salary FROM employees e inner join salaries s on e.emp_no=s.emp_no;
    END//
    delimiter ;
    :return:
    """
    cnx = connect_default()
    cursor = cnx.cursor()

    cursor.execute("call list_all_employees_with_salary()")
    results = cursor.fetchall()
    print(tabulate(results, headers=['ID', 'DOB', 'First Name', 'Last Name', 'Gender', 'Hire Date', 'Salary']))


def execute_procedure_update_salary_of_employee():
    """
    Execute procedure update_salary_of_employee
    delimiter //
    CREATE PROCEDURE update_salary_of_employee(emp_no int, salary int)
    BEGIN
        UPDATE salaries set salaries.salary=salary where salaries.emp_no=emp_no;
    END//
    delimiter ;
    :return:
    """
    cnx = connect_default()
    cursor = cnx.cursor()
    emp_no = input("Input employee id: ")
    salary = input("Input new salary for employee: ")
    try:
        cursor.callproc("update_salary_of_employee", (emp_no, salary))
        print("Update salary successfully!")
    except Exception as e:
        print("Error when update salary", e)


def promote_employee():
    """
    Execute procedure update_salary_of_employee
    delimiter //
    CREATE PROCEDURE update_salary_of_employee(emp_no int, salary int)
    BEGIN
        UPDATE salaries set salaries.salary=salary where salaries.emp_no=emp_no;
    END//
    delimiter ;
    :return:
    """
    cnx = connect_default()
    cursor = cnx.cursor()
    emp_no = input("Input employee id: ")
    try:
        emp_no = int(emp_no)
    except ValueError:
        print("Invalid emp_no")
        return
    cursor.execute("select salary from salaries where emp_no=%s" % emp_no)
    salary = cursor.fetchone()[0]
    try:
        cursor.callproc("update_salary_of_employee", (emp_no, salary))
        print("Update salary successfully!")
    except Exception as e:
        print("Error when update salary", e)


def execute_procedure_update_title_of_employee():
    """
    Execute procedure update_title_of_employee
    delimiter //
    CREATE PROCEDURE update_title_of_employee(emp_no int, title varchar(50))
    BEGIN
        UPDATE titles set titles.title=title where titles.emp_no=emp_no;
    END//
    delimiter ;
    :return:
    """
    cnx = connect_default()
    cursor = cnx.cursor()
    emp_no = input("Input employee id: ")
    salary = input("Input new title for employee: ")
    try:
        cursor.callproc("update_title_of_employee", (emp_no, salary))
        print("Update title successfully!")
    except Exception as e:
        print("Error when update title", e)


def find_highest_salary():
    """
    Execute function highest_salary
    delimiter //
    CREATE FUNCTION highest_salary()
    BEGIN
        DECLARE max_salary int;
        SELECT max(salary) into max_salary FROM salaries;
        return max_salary;
    END//
    delimiter;
    :return: 
    """
    cnx = connect_default()
    cursor = cnx.cursor()

    cursor.execute("select highest_salary();")
    result = cursor.fetchone()
    print(f"Highest salary is: {result[0]}")


def delete_employee():
    cnx = connect_default()
    cursor = cnx.cursor()
    emp_no = input("Input emp_no for delete: ")
    try:
        emp_no = int(emp_no)
    except ValueError:
        print('Invalid value for emp_no')
    delete_emp = "DELETE FROM employees where emp_no=%(emp_no)s"
    delete_salary = "DELETE FROM salaries where emp_no=%(emp_no)s"

    # Insert salary information
    data = {
        'emp_no': emp_no,
    }
    cursor.execute(delete_salary, data)
    cursor.execute(delete_emp, data)

    cnx.commit()


def select_salaries_of_employees():
    emp_ids = input("Input employees id (separate by,): ")
    try:
        [int(emp_id) for emp_id in emp_ids.split(',')]
    except ValueError as e:
        print("Invalid employees id ...", e)
        return
    cnx = connect_default()
    cursor = cnx.cursor()
    cursor.execute("SELECT first_name, last_name, salary from employees e inner join salaries s on e.emp_no = "
                   "s.emp_no where s.emp_no in (%s)" % emp_ids)
    results = cursor.fetchall()
    print(tabulate(results, headers=['First Name', 'Last Name', 'Salary']))


def move_employee_to_department():
    """
    create procedure move_employee(emp_no int, dept_name varchar(40))
    begin
        declare v_dept_no char(4) default null;
        select dept_no into v_dept_no from departments where departments.dept_name=dept_name;
        if v_dept_no is not null then
            update dept_emp set dept_no=v_dept_no where dept_emp.emp_no=emp_no;
        end if;
    end//
    :return: 
    """
    emp_no = input("Input emp id to move to new department: ")
    try:
        emp_no = int(emp_no)
    except ValueError:
        print("Invalid emp id")
        return
    dept_name = input("Input new department name for employee: ")
    cnx = connect_default()
    cursor = cnx.cursor()
    cursor.callproc('move_employee', (emp_no, dept_name))
    cnx.commit()


def ask_for_absent_a_day():
    emp_no = input("Input emp_no for absent: ")
    insert_absent(emp_no)


def ask_for_absent_a_noon():
    emp_no = input("Input emp_no for absent: ")
    hours = input("Input hours of absent (1-8): ")
    try:
        hours = int(hours)
    except ValueError:
        print("Invalid hours for absent")
        return
    insert_absent(emp_no, abs_hours=hours)


def add_employee_to_absent():
    emp_no = input("Input emp_no for absent: ")
    insert_absent(emp_no, has_form=False)


if __name__ == '__main__':
    functions = {
        '1': input_insert_location,
        '2': input_insert_dept,
        '3': input_insert_employee,
        '4': input_insert_dept_emp,
        '5': input_insert_salary,
        '6': input_insert_title,
        '7': input_insert_employee_and_salary,
        '8': input_insert_employee_salary_and_title,
        '9': delete_employee,
        '10': find_highest_salary,
        '11': execute_procedure_list_all_employees,
        '12': execute_procedure_list_all_employees_with_salary,
        '13': select_salaries_of_employees,
        '14': execute_procedure_update_salary_of_employee,
        '15': promote_employee,
        '16': move_employee_to_department,
        '17': ask_for_absent_a_day,
        '18': ask_for_absent_a_noon,
        '19': add_employee_to_absent,
        '99': exit
    }
    while True:
        print("Options for interact with application from menu: ")
        print("\t1) Insert location")
        print("\t2) Insert department")
        print("\t3) Insert employee")
        print("\t4) Insert department and employee")
        print("\t5) Insert salary for employee")
        print("\t6) Insert title for employee")
        print("\t7) Insert employee and salary for employee")
        print("\t8) Insert employee, salary and title for employee")
        print("\t9) Delete employee")
        print("\t10) Find highest salary")
        print("\t11) Select all employees")
        print("\t12) Select employees with salary")
        print("\t13) Select salaries of employees")
        print("\t14) Update salary of employee")
        print("\t15) Promote employee")
        print("\t16) Move employee to new department")
        print("\t17) Ask for absent a day")
        print("\t18) Ask for absent a part of day")
        print("\t19) Add employee absent (employee not ask or email for absent - reduce salary in this month)")
        print("\t99) Exit application")
        x = input("Select option: ")
        if x not in functions.keys():
            print("Option not found. Please try again.")
            continue
        functions[x]()
