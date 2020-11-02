import io
import os
import csv
import datetime
from flask import render_template, json, redirect, url_for, request, flash
from app import app
from app.services import add_employees, get_employees
from app.utils import save_file, check_filetype, parse_csv
from config import DATA_DIR


@app.route('/')
@app.route('/employees', methods=["GET", "POST"])
def index():

    employees = get_employees()

    if request.method == 'POST':

        salary_from = None
        if 'salary-from' in request.form and request.form['salary-from']:
            salary_from = int(request.form['salary-from'])

        salary_to = None
        if 'salary-to' in request.form and request.form['salary-to']:
            salary_to = int(request.form['salary-to'])

        order_by = 'id'
        if 'order_by' in request.form:
            order_by = request.form['sort-by']

        employees = get_employees(max_salary=salary_to, min_salary=salary_from, order_by=order_by)

    return render_template('employees.html', employees=employees)


@app.route('/upload', methods=["GET", "POST"])
def upload():

    if request.method == 'POST':
        file = request.files['file']
        if file and check_filetype(file):
            filepath = save_file(DATA_DIR, file)
            employees = parse_csv(filepath)
            print(employees)
            add_employees(employees)

    return render_template('upload.html')

