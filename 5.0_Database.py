""" Let's explore how to create a database connection in Flask by using SQLAlchemy
Until now we have been using some data structures like a dictionary, but in real-world apps that's not really a normal approach.
We'll instead use a SQL database and an object relation mapper to maniuplate it.

An Object Relational Mapper(ORM) makes writing SQL queries easier for a programmer.  It enables us to write queries
in an object-oriented langaugae.  The ORM automatically translates it to SQL and retrieves the result in the form of objects

SQLAlchemy is as library in Python which allows us to mainpulate SQL.  It provides us with an easy to use ORM for SQL databases.

Flask-SQLAlchemy is a Flask specific library that integrates SQLAlchemy support with flask apps.
It provides extra helpers for common tasks that make it easier to work with flask.
"""

# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm
from flask import Flask, render_template
from flask_sqlAlchemy import SQLAlchemy

""" Set the config variable to the database file:
Set a configuration variable in the application so that the app knows where the database file is located.
Here we use SQLite
The name will contain the prefix sqlite:/// followed by the path.
You could use another databse with SQLAlchemy as well.
Set the config variable SQLALCHEMY_DATABASE_URI to point to this file
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'


# initialize the connection by creating an object of the SQLAlchemy class

database = SQLAlchemy(app)

# app.py full implementation:

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", message="Successfully Logged In")
        return render_template("login.html", message="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# This helped us create to the database


""" Getting started with Models:
Earlier we learned about views, templates and models.
Previously we covered views and templates, let's talk models.

"""

# create a model class for User
# create a class for a User table.  It'll inherit from the model class from SQLAlchemy


class User(db.Model):

    # add colums for the table.
    # define the data type
    # set a null value if nothing is there
    # check for uniqueness
email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
password = db.Column(db.String, nullable=False)

# create a table in a database
db.create_all()


# Complete implementation for app.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


db.create_all()

users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", message="Successfully Logged In")
        return render_template("login.html", message="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


""": One-to-Many Relationship:
Let's learn how to add a one-to-many relationship between models.
There's three relationships
One-to-many
One-to-one
Many-to-many

Let's cover how to represent and create these relationsihps using SQLAlchemy
"""

# a simple implementation of these models is given below:


class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)


class Department(db.Model):
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(120), nulllable=False)


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)


# create a column containing ForeignKey().
class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    department_name = db.Column(db.String(50), db.ForeignKey(
        'department.name'), nullable=False)


# create a relationship() column
class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee')
# add the backref argument.
# last step we provided relationship() column in the Department model.
# have not yet specified which rows of the Employee are associated with a row of Department.
# To associate it, add a backref argument to relationship() function

# Complete Implementattion
# We can observe a one-to many relationship between Employee and Department


class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    department_name = db.Column(db.String, db.ForeignKey(
        'department.name'), nullable=False)


class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee', backref='department')


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)


""" One to One relationship:
A one-to-one relationship should exist between Employee and Department.
This relationship will indicate that one and only one employee can be the head of the department

Steps:
- Create a column containing ForeignKey()
"""


class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    department_name = db.Column(db.String, db.ForeignKey(
        'department.name'), nullable=False)
    # add the ForeignKey column to Employee
    is_head_of = db.Column(db.String, db.ForeignKey(
        'department.name'), nullable=True)


# create a relationship() column with backref
# add backref that can be used by the employee to access the department row
class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee', backref='department')
    # add relationship() with the Employee table and a backref called head_of_department
    head = db.relationship('Employee', backref='head_of_department')

# Set useList parameter to False:
# This differentiates it from a one-to-many relationship.  Make sure that this relationship is not built
# with more than one employee.
# add an extra argument to the function called useList and set it to False.  This ensures it will not point to a list.\


class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee', backref='department')
    # set the useList parameter of the relationship() to false
    head = db.relationship(
        'Employee', backref='head_of_department', uselist=False)


# complete implementation

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    department_name = db.Column(db.String, db.ForeignKey(
        'department.name'), nullable=False)
    # added this
    is_head_of = db.Column(db.String, db.ForeignKey(
        'department.name'), nullable=True)


class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee', backref='department')
    # added this
    head = db.relationship(
        'Employee', backref='head_of_department', uselist=False)


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)


"""Question:

What is the type of the relationship which exists between Entity1 and Entity2 in the snippet given below?

class Entity1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    column1 = db.Column(db.String, db.ForeignKey('entity2.id'))
        
class Entity2(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    column2 = db.relationship('Entity1', backref='column3', uselist=True)

A: One to many
"""
