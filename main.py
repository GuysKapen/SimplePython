from connector import connect_default
from insert_data import insert_employee, insert_salary


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


def input_insert_employee_and_salary():
    emp_no = input_insert_employee()
    input_insert_salary(emp_no)


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
    for row in cursor.fetchall():
        print('\t\t'.join(map(lambda data: str(data), row)))


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
    except ValueError as e:
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


if __name__ == '__main__':
    functions = {
        '1': input_insert_employee,
        '2': input_insert_salary,
        '3': input_insert_employee_and_salary,
        '4': delete_employee,
        '5': find_highest_salary,
        '6': execute_procedure_list_all_employees,
        '99': exit
    }
    while True:
        print("Options for interact with application from menu: ")
        print("\t1) Insert employee")
        print("\t2) Insert salary for employee")
        print("\t3) Insert employee and salary for employee")
        print("\t4) Delete employee")
        print("\t5) Find highest salary")
        print("\t6) Select all employees")
        print("\t99) Exit application")
        x = input()
        if x not in functions.keys():
            print("Option not found. Please try again.")
            continue
        functions[x]()
