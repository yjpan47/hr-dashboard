from app import db
from app.models import Employee


def add_employee(employee):
    try:
        curr_employee = Employee.query.filter_by(id=employee.id).first()
        if curr_employee:
            db.session.delete(curr_employee)
        db.session.add(employee)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(f"Error in adding employee to the database. Message: {e}")


def get_employees(min_salary=None, max_salary=None, order_by='id'):
    try:
        employees = Employee.query.all()
        if min_salary:
            employees = list(filter(lambda employee: employee.salary >= min_salary, employees))
        if max_salary:
            employees = list(filter(lambda employee: employee.salary >= max_salary, employees))
        if order_by == 'id':
            employees.sort(key=lambda employee: employee.id)
        if order_by == 'login':
            employees.sort(key=lambda employee: employee.login)
        if order_by == 'name':
            employees.sort(key=lambda employee: employee.name)
        if order_by == 'salary':
            employees.sort(key=lambda employee: employee.salary)
        return list(map(lambda employee: {
            'id': employee.id,
            'name': employee.name,
            'login': employee.login,
            'salary': round(employee.salary, 2)
        }, employees))

    except Exception as e:
        db.session.rollback()
        print(f"Error in adding employee to the database. Message: {e}")


def add_employees(employees):
    for employee in employees:
        add_employee(employee)
