# HR Employees

This project is built with Flask (full-stack).

`python3` and `pip3` will be used to indicate that we are using Python 3. Your commands may be different.
Please make sure virtualenv is installed.

Running the project from root dir:

### 1. Start a virtual environment

```
python3 -m venv venv
```

### 2. Activate virtual environment

```
source venv/bin/activate
```

### 3. Install Flask and dependencies

```
pip3 install flask
pip install -r requirements.txt
```

### 4. Set environment variables

```
export FLASK_APP=main.py
```

### 5. Set Database

Ensure that Flask-SQLAlchemy and Flask-Migrate are installed.
```
pip3 install flask-sqlalchemy
pip3 install flask-migrate
```

Create a database migration folder. 
```
flask db init
```
Next, generate a migration script.
```
flask db migrate
```
Then, generate the SQL tables by running the **upgrade** command.
```
flask db upgrade
```

### 6. Run flask

```
flask run
```
