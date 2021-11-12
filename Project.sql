create user 'guys'@'localhost' identified by 'Python@Guys';
grant all on employees.* to 'guys'@'localhost';

create database employees;
use employees;

delimiter //
CREATE PROCEDURE list_all_employees()
BEGIN
    SELECT * FROM employees;
END//
delimiter ;

drop procedure list_all_employees_with_salary;
delimiter //
CREATE PROCEDURE list_all_employees_with_salary()
BEGIN
    SELECT e.*, s.salary
    FROM employees e
             inner join salaries s on e.emp_no = s.emp_no;
END//
delimiter ;
-- Test
call list_all_employees_with_salary();

delimiter //
CREATE PROCEDURE update_salary_of_employee(emp_no int, salary int)
BEGIN
    UPDATE salaries set salaries.salary=salary where salaries.emp_no = emp_no;
END//
delimiter ;

delimiter //
CREATE FUNCTION highest_salary()
    returns float
    READS SQL DATA
    DETERMINISTIC
BEGIN
    DECLARE max_salary float;
    SELECT max(salary) into max_salary FROM salaries;
    return max_salary;
END//
delimiter ;


delimiter //
create procedure move_employee(emp_no int, dept_name varchar(40))
begin
    declare v_dept_no char(4) default null;
    select dept_no into v_dept_no from departments where departments.dept_name = dept_name;
    if v_dept_no is not null then
        update dept_emp set dept_no=v_dept_no where dept_emp.emp_no = emp_no;
    end if;
end//
delimiter ;

delimiter //
CREATE PROCEDURE list_employees_abs_more_than_allow()
BEGIN
    select e.*,
           month(employees_absent.abs_date) as month,
           year(employees_absent.abs_date)  as year,
           sum(abs_hours)                   as sum_abs_hours
    from employees_absent
             inner join employees e
                        on employees_absent.emp_no = e.emp_no
    group by e.emp_no, month, year
    having sum_abs_hours >= 32;
END//
delimiter ;


delimiter //
CREATE PROCEDURE list_employees_abs_more_than_allow()
BEGIN
    select e.*,
           month(employees_absent.abs_date) as month,
           year(employees_absent.abs_date)  as year,
           AVG(abs_hours)                   as avg_abs_hours
    from employees_absent
             inner join employees e
                        on employees_absent.emp_no = e.emp_no
    group by e.emp_no, month, year;
END//
delimiter ;


delimiter //
CREATE PROCEDURE list_employees_abs_more_than_allow()
BEGIN
    select e.*, (s.salary - salary / 30 * (sum(abs_hours) / 8)) as current_month_salary
    from salaries s
             inner join employees e on s.emp_no = e.emp_no
             inner join employees_absent ea on e.emp_no = ea.emp_no
    where month(ea.abs_date) = month(sysdate())
    group by e.emp_no, s.salary;
END//
delimiter ;


delimiter //
CREATE FUNCTION find_real_salary_of_employee_in_current_month(emp_no int) returns float
BEGIN
    declare real_salary float;
    select s.salary - salary / 30 * (sum(abs_hours) / 8)
    into real_salary
    from salaries s
             inner join employees e on s.emp_no = e.emp_no
             inner join employees_absent ea on e.emp_no = ea.emp_no
    where month(ea.abs_date) = month(sysdate())
      and e.emp_no = emp_no
    group by e.emp_no;
    return real_salary;
END//
delimiter ;

delimiter //
CREATE FUNCTION find_budget_salary_in_current_month() returns float
BEGIN
    declare sum_real_salary float;
    select sum(current_month_salary)
    into sum_real_salary
    from (select (s.salary - salary / 30 * (sum(abs_hours) / 8)) as
                     current_month_salary
          from salaries s
                   inner join employees e on s.emp_no = e.emp_no
                   inner join employees_absent ea on e.emp_no = ea.emp_no
          where month(ea.abs_date) = month(sysdate())
          group by e.emp_no, s.salary) real_salaries;
    return sum_real_salary;
END//
delimiter ;