# Handling forms in Flask

"""
We will learn about two methods of handling forms in Flask
- Via the request object
- Via the Flask-WTF extension

"""

"""Using the request object:
With an example login form, create a template and route for this form
"""

# html template with email and password fields, as well as submit button
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, EqualTo
from forms import SignUpForm
from flask import Flask, render_template, abort
from forms import LoginForm
from forms importLoginForm
from wtforms.validators import InputRequired, Email
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import Flaskform
from flask import Flask, render_template
from flask import request
from flask.templating import render_template
from flask.helpers import _PackageBoundObject
from flask import Flask, render_templat
<h1 > Login < /h1 >
<form method = "POST" >
    Email: < br >
    <input type = "text" name = "email" >
    <br >
    Password: < br >
    <input type = "password" name = "password" >
    <br > <br >
    <input type = "submit" value = "Login" >
</form >

# create a new route for login
# app.py
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# base.html
<!DOCTYPE html >
<html lang = "en" >
<head >
    <link rel = "stylesheet" href = "{{url_for('static', filename='format.css')}}" / >
    <title > {% block title % }{ % endblock % } - Jinja Demo < /title >
    {% block head % }
    {% end block % }

</head >
<body >
   <div >
       <ul >
            <li > <a href = "{{url_for('home')}}" > Home < /a > </li >
            <li > <a href = "{{url_for('login')}}" > Login < /a > </li >
        </ul >
    </div >
    <div id = "header"> FORMS DEMO </div>
    <div id = "content">
        { % block content % }
        { % endblock % }
           </div >
    <div id = "footer"> Copyright ... </div>
</body >
</html >

# home.html

# extend the base html page
{% extends "base.html"}

{ % block title % }
Home Page
{ % endblock % }

{ % block content % }
<h1 > Home Page < /h1>
<p > Welcome to the Jinja2 demo</p>
{ % endblock % }

# login.html
{ % extends "base.html" % }

""" Data Handling using the request object:
Let's handle the POST request received by the login template and retrieve the data
"""

# start by importing request

# use the method member variable of the request object to determine the method of an incoming request


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        ...
    else:
        ...
    return render_template("login.html")


"""
We checked to see if the method is POST.  
Then the logic for handling POST request can be implmented.
If the request is not POST, there's another block for logic to handle other requests
"""

"""
We can use the form member vairable of the request object to obtain values that the user submitted.
The form vairbale is a special data structure called ImmutableMultiDict"
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # notice the syntax for extracting the form data.
        # the key for form dictionary corresponds to the name attribute of <input> tag.
        email = request.form["email"]
        password = request.form["password"]
        ...
    else:
        ...
    return render_template("login.html")


# another way of writing this logic would be
if request.method == "POST":
    email = request.form.get("email")
    password = request.form.get("password")


# example app.py where user credentials are stored in the form of a dictionary
app = Flask(__name__)

# dictionary of users
users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # for validation check to see if email exists as a key in the dictionary associated with the value of password
        if email in users and users[email] == password:
            return render_template("login.html", message="Successfully Logged In")
        return render_template("login.html", message="Incorrect Email or Password")
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# Create forms using Flask-WTF and WTForms
# In the last example it was somewhat oversimplified.  In this one, we will go ahead and add checks
# to write the logic for inside the login view

# WTForms is a library that makes form handling easy.  It handles form validation and form redering at the front-end
# Flask-WTF is a Flask specific library that integrates the WTForm library with Flask.  It acts as an
# add on to WTForms and adds some extra components, such as security

# In this lesson we will be using Flask-WTF in conjunction with WTForms to handle forms

# import it

# create LoginForm class.  For each form in the website we will create a form.  This class will inherit from FlaskForm


class LoginForm(FlaskForm):
    ...


""" login form components
- An input field for email
- An input field for password
- The submit button field

For each possible field, wtforms has associated classes.

StringField for email
PasswordField for password
SubmitField for submit button
"""

# import all those classes:

# make instances of these classes as member variables of our class and pass labels of these fields as input to constructors


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Login')


"""Add field validators from wtforms
Validators are the rules and checks we want to apply to a field inside the form.
For example, with an email filed we want to check if the email is valid.
"""

# import the two checks we will use in this example

# apply these validators to the fields.  Provide a list of parameters to them:


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
    # InputRequired() sets the required attribute in html
    # Email() checks if the given input is a valid email

# here's the complete implementation of forms.py




class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


"""Rendering Flask-WTF forms in templates:
"""

# import LoginForm from module forms.py into app.py


# create an object of LoginForm in the login view

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

# pass the form to the render_template function as a named argument


@app.route("/login", mothods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


# login.html
# Use Jinjas syntax to reder the form instance of LoginForm
{{form.field_name}}

# replace the HTML code with new syntax:
<form action = "{{url_for('login')}}" method="POST">
    {{ form.email.label }}: < br >
    {{form.email }}
    <br >
    {{ form.password.label }}: < br >
    {{form.password}}
    <br >
    {{form.submit}}
</form >

# prevent against cross-site request forgery by adding the csrf_token

<form action = "{{url_for('login')}}" method="POST">
    {{ form.email.label }}: < br >
    {{form.email }}
    <br >
    {{ form.password.label }}: < br >
    {{form.password}}
    <br >
    {{form.csrf_token}}
    {{form.submit}}
</form >


"""Form Validation and Data and Error Handling with Flask-WTF:
Let's learn how to validate the data received from the form and how to handle validation errors.


form.is_submitted()
This function is inherited from the WTForms module.  It returns true if the form was submitted, therefore if it's a GET request than this will always be false.
This is how we differentiate between GET and POST

form.validate()
This returns true if all the conditions specified in the validators have been met.

form.validate_on_submit()
This function is a shortcut function that Flask-WTF contains that returns true if both 
form.is_submitted() and form.validate() return true

"""


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

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
    # use the functions we just learned about
    if form.is_submitted():
        print("Submitted.")

    if form.validate():
        print("Valid.")

    if form.validate_on_submit():
        print("Submitted and Valid.")

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


""" Error Handling:
forms.erros is used.  We can get individual errors for each field by using
form.field_name.errors
"""


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

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
        print("Submitted and Valid.")
    # use forms.error:
    elif forms.errors:
        print(form.errors.items())
        print(form.email.errors)
        print(form.password.errors)
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# the above example will output errors for the form fields that are not input correctly

# We can also deisplay the validaton error messages at the login template

"""Data handling:
We can obtain the inputs by using field_name.data"""


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

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
        # use field_name.data
        print("Email:", form.email.data)
    elif form.errors:
        print(form.errors.items())
        print(form.email.errors)
        print(form.password.errors)
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# Complete implementation of user authentication.  We can implement the same thing using the data and error handling methods:


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

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
        return render_template("login.html", form=form, message ="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


"""The method form.validate_on_submit() is a shortcut for which two functions?
A:  form.is_submitted() and form.validate()
"""

"""Project Challenge: Render a sign-up form and navbar

Add a sign-up form to the application using Flask-WTF and reder it on a template

Create a sign-uip form that should have 4 fields:
-Full Name
-Email
-Password
-Confirm Password
-Submit

Assosciate necessary validators with them
Implement a horizontal navabar on top of each page with 3 links:
-Home
-About
-Sign Up

"""

# Given app.py
"""Flask Application for Paws Rescue Center."""
app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
    {"id": 1, "name": "Nelly", "age": "5 weeks",
        "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
    {"id": 2, "name": "Yuki", "age": "8 months",
                "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
    {"id": 3, "name": "Basker", "age": "1 year",
                "bio": "I love barking. But, I love my friends more."},
    {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
]


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html", pets=pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """View function for Showing Details of Each Pet."""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet=pet)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# Solution app.py
"""Flask Application for Paws Rescue Center."""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

"""Information regarding the Pets in the System."""
pets = [
    {"id": 1, "name": "Nelly", "age": "5 weeks",
        "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
    {"id": 2, "name": "Yuki", "age": "8 months",
                "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
    {"id": 3, "name": "Basker", "age": "1 year",
                "bio": "I love barking. But, I love my friends more."},
    {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
]


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html", pets=pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """View function for Showing Details of Each Pet."""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet=pet)

# add the view function signup.  Associate with the route /signup and make it accept both GET and POST methods.


@app.route("/signup", methods=["POST", "GET"])
def signup():
    """View function for Showing Details of Each Pet."""
    form = SignUpForm()
    return render_template("signup.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
# forms.py solution

# create a SignUpForm class that inherits from FlaskForm.


class SignUpForm(FlaskForm):
    # it has the same fields as the previous example, but with two more.
    full_name = StringField('Full Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html", pets=pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """View function for Showing Details of Each Pet."""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet=pet)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# signup.html pre-implementation:
{ % extends "base.html" % }

{ % block title % }
Sign-Up
{ % endblock % }

{ % block heading % }
Sign Up
{ % endblock % }

{ % block content % }

# sign-up.html post-implementation

# extend the base.html
{ % extends "base.html" % }

{ % block title % }
Sign-Up
{ % endblock % }

{ % block heading % }
Sign Up
{ % endblock % }

{ % block content % }
# inherit the signup.html template
<form action = "{{url_for('signup')}}" method="POST" style="padding:5px;">
   <!-- Full Name Field - ->
    {{ form.full_name.label }}: < br >
    {{form.full_name }}
    <br >
    <!-- Email Field - ->
    {{ form.email.label }}: < br >
    {{form.email }}
    <br >
    <!-- Password Field - ->
    {{ form.password.label }}: < br >
    {{form.password}}
    <br >
    <!-- Confirm Password Field - ->
    {{ form.confirm_password.label }}: < br >
    {{form.confirm_password}}

       <!-- Hidden CSRF Token Field - ->
    {{form.csrf_token}}
    <br >
       <!-- Submit Field - ->
    {{form.submit}}
</form >
{ % endblock % }

"""Signup.html had 2 major changes:
- Display errors: to display error messages that indicate validation failure, a for loop in Jinja printed all the errors
associated with a field underneath it.
- Display success message: as mentioned, if the new_user is added to the users, a variable called message is sent to indicate success.
We then check to see if the variable was received
"""


"""Project Challenge: create a Login and Logout Mechanism
- Add a login and logout mechanism to the application
To differentiate between one request and another sessions are used in Flask.  Session stores information regarding each transaction in 
the form of cookies.
In Flask we use the global session object to access the current session.
The object is a dictionary that can have keys added or removed from it.
For example, when a user logs in we can insert a 'user' key in the session with the value of the current user's object.
When they logout, we can remove the 'user' key from the session.

Tasks in this challenge:
- Authentication: the user should be authenticated using the data received from the form in the login view.
Match information from the users to authenticate
- Invalid user data: in the case of wrong credentials, the login view should send a message to the template saying "Wrong credentials.  Please try again"
- Valid user data: in the case of valid user data, return the message" successfully logged in!"
- Initialize user in the session: also in the case of successful authentication, add the 'user' key in the session object before returnin the template
- Logout view and user removed from session: Give a mechanism to logout.
Create a 'logout' view function and route.  It should log the user out by removing the 'user' key from the session
dictionary and logout view should redirect to the homepage view
- Logout button in the navbar: if the user is logged in, give them the option of logout instead of 'sign up' and 'login' buttons in the nav bar

Note: Flask provides us with a redirect() function, which we can use to return a view instead of a template.  This function takes the URL for the view
we want to redirect to.  Use the url_for() to create this URL.  Add the following arguments for security
return redirect(url_for('view_name', scheme='https', _external=True))
"""

# pre-implementation app.py
"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template, abort
from forms import SignUpForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

"""Information regarding the Users in the System."""
users = [
            {"id": 1, "full_name": "Pet Rescue Team", "email": "team@pawsrescue.co", "password": "adminpass"},
        ]


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html", pets = pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """View function for Showing Details of Each Pet.""" 
    pet = next((pet for pet in pets if pet["id"] == pet_id), None) 
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    """View function for Showing Details of Each Pet.""" 
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("signup.html", message = "Successfully signed up")
    return render_template("signup.html", form = form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    return render_template("login.html", form = form)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# app.py solution

"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template, abort
from forms import SignUpForm, LoginForm
# import sessio, redirect and url_for
from flask import session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

"""Information regarding the Users in the System."""
users = [
            {"id": 1, "full_name": "Pet Rescue Team", "email": "team@pawsrescue.co", "password": "adminpass"},
        ]


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html", pets = pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """View function for Showing Details of Each Pet.""" 
    pet = next((pet for pet in pets if pet["id"] == pet_id), None) 
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    """View function for Showing Details of Each Pet.""" 
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("signup.html", message = "Successfully signed up")
    return render_template("signup.html", form = form)

# make changes to the login view
@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    # check to see if the form is valid and the user is authenticated
    if form.validate_on_submit():
        user = next((user for user in users if user["email"] == form.email.data and user["password"] == form.password.data), None)
        # search for the user and make a loop to handle the situations
        # if the user is not found, display the message
        if user is None:
            return render_template("login.html", form = form, message = "Wrong Credentials. Please Try Again.")
        # if the user is found, authenticate the user by adding it to the session object with the key 'user'
                else:
            session['user'] = user
            return render_template("login.html", message = "Successfully Logged In!")
    return render_template("login.html", form = form)

# insert logout route of /logout
@app.route("/logout")
def logout():
    # check to see if the user is present in the session.
    if 'user' in session:
        # remove the user
        session.pop('user')
    # redirect the user to the homepage view using redirect and url_for() function
    return redirect(url_for('homepage', _scheme='https', _external=True))
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# base.html pre-implementation
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{% block title %} {% endblock %} - Paws Rescue Center</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />  
</head>
<body>
    <div>
        <ul style="list-style-type: none;float: right;font-size: large;">
            <li style="display:inline"><a href="{{url_for('homepage')}}">Home</a></li>
            <li style="display:inline"><a href="{{url_for('about')}}">About</a></li>
            <li style="display:inline"><a href="{{url_for('signup')}}">Sign Up</a></li>
            <li style="display:inline"><a href="{{url_for('login')}}">Login</a></li>
        </ul>
    </div>
    <h1 id="title"> {% block heading %} {% endblock %} </h1>
    <div id="content">
        {% block content %} {% endblock %}
    </div>
</body>
</html>

# base.html post-implementation

# use base.html to modify the navbar in the case of a logged in user.
# use the if statement in Jinja to check if 'user' is present in the session.
# if present, add a link to the logout route
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{% block title %} {% endblock %} - Paws Rescue Center</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />  
</head>
<body>
    <div>
        <ul style="list-style-type: none;float: right;font-size: large;">
            <li style="display:inline"><a href="{{url_for('homepage')}}">Home</a></li>
            <li style="display:inline"><a href="{{url_for('about')}}">About</a></li>
            # create the iff statement to check if the user is logged into the session
            {% if 'user' in session %}
            <li style="display:inline"><a href="{{url_for('logout')}}">Log Out</a></li>
            {% else %}
            <li style="display:inline"><a href="{{url_for('signup')}}">Sign Up</a></li>
            <li style="display:inline"><a href="{{url_for('login')}}">Login</a></li>
            {% endif%}
        </ul>
    </div>
    <h1 id="title"> {% block heading %} {% endblock %} </h1>
    <div id="content">
        {% block content %} {% endblock %}
    </div>
</body>
</html>

