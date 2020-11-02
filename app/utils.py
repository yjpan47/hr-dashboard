import os
import pandas as pd

from app.models import Employee


def check_filetype(file):
    file_name, file_ext = os.path.splitext(file.filename)
    return file_ext == '.csv'


def save_file(directory, file, filename='employee.csv'):
    try:
        filepath = os.path.join(directory, filename)
        file.save(filepath)
        return filepath
    except Exception as e:
        return f"Error in saving file. Message: {e}"


def parse_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        columns = df.columns
        if len(columns) != 4:
            raise ValueError("Invalid table schema")
        for col in columns:
            if df[col].isnull().values.any():
                raise ValueError("Null values in table")
        employees = []
        for index, row in df.iterrows():
            id, login, name, salary = row[0], row[1], row[2], row[3]
            if type(id) != str or type(login) != str or type(name) != str or type(salary) != float:
                raise ValueError(f"Invalid value types at row {index}")
            employee = Employee(id=id, login=login, name=name, salary=salary)
            employees.append(employee)
        return employees
    except Exception as e:
        return f"Error in parsing csv. Message: {e}"

