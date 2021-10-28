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


if __name__ == '__main__':
    functions = {
        '1': input_insert_employee,
        '2': input_insert_salary,
        '3': input_insert_employee_and_salary,
        '4': insert_employee,
        '5': insert_salary,
        '99': exit
    }
    while True:
        print("Select options for interact with application from menu: ")
        print("\t1) Insert employee")
        print("\t2) Insert salary for employee")
        print("\t3) Insert employee and salary for employee")
        print("\t4) Delete employee")
        print("\t4) Insert department")
        print("\t99) Exit application")
        x = input()
        if x not in functions.keys():
            print("Option not found. Please try again.")
            continue
        functions[x]()
