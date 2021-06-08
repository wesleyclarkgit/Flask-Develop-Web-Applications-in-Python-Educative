# Let's learn about dynamic templates and jinja's templating engine

"""
Until now we have learned how to serve static HTML templates and other static files such as images, css.
Dynamic template use case:  Consider that if we are making an app with multiple users, each user will have a unique profile associated with them.
The web app must serve a unique template containing the corresponding user logged in.
One way to implement this would be to use a genereric template containing a variable rule.
When the template is rendered on the client-side, an appropriate value is placed instead of the rule.
This new value is per the context of the application(the info of currently logged-in user).
This kind of dynamic behavior of a template is dynamic routing.
Flask has built in dynamic templating engine, Jinja.

Jinja:
Jinja is a template engine that lets us serve dynamic data to the template files.
A template file is a text file that does not have a particular extension.
There's a few delimiters that we need to know with Jinja Syntax:
-{% ... %} used for statements
{{ ...}} used for variables
{{# ...}} used for comments
# ... ## is used for line statements
"""

# Variables
"""
Flask allows us to pass any Python object to the template which can then be referred to inside the template using Jinja syntax
We can use variables inside the templates using two steps
- The object is provided as a named argument to the render_template() function
return render_template("index.html", my_object = Object)
- The value of this object is then fetched inside the template using the {{}} syntax
{{ my_object }}
"""
# example: a string variable called Username

# app.py
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    # declare the username Sally
    Username = "Sally"
    return render_template("index.html", username=Username)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# index.html

<!DOCTYPE html >
<html lang = "en" >
<head >
    <meta charset = "utf-8" >
    <title > Jinja2 Demo < /title >
</head >
<body >
    <h3 > Username: < /h3 >
    <p >
        # use the jinja syntax to call a Python variable that is declared in app.py
        {{username}}
    </p >
</body >
</html >


# Control Flow:  Let's learn how to add control flow blocks in Jinja

"""
Jinja provides syntax to handle control flow of the application inside templates.  Loops and conditions can be added to the templates in Pythonic syntax
"""

# Loops
{% for elements in array % }
...
{% endfor % }

# Consider the example of a dictionary that can be traversed using loops
# index.html

<!DOCTYPE html >
<html lang = "en" >
<head >
    <meta charset = "utf-8" >
    <title > Jinja2 Demo < /title >
</head >
<body >
   <table style = "width:100%; text-align:center" >
    <tr >
         <th > Index < /th >
        <th>Username</th>
        <th>Location</th>
    </tr>
    {% for username, location in users.items() %}
    <tr>
        <td>{{loop.index}}</td>
        <td>{{username}}</td>
        <td>{{location}}</td>
    </tr>
    {% endfor %}
</table>
</body>
</html>


""" Conditional:
{% if true %}
{% endif %}
Note: you always end the if condition using endif

For multiple branches of conditions, else and elif can be used
{% if ... %}
{% elif ... %}
{% else %}
{% endif %}
"""

# Here's an example if we only want to show the users at the location of Los Angelas
# index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Jinja2 Demo</title>
</head>
<body>  
   <table style="width:100%; text-align:center">
    <tr>
        <th>Username</th>
        <th>Location</th>
    </tr>
    {% for username, location in users.items() %}
    { if location == "Los Angelas" %}
    <tr>
        <td>{{username}}</td>
        <td>{{location}}</td>
</table>
</body>
</html>

# Next we learn about template inheritance

"""Template Inheritance:
Template Inheritance is a compelling feature of Jinja that lets us reuse templates.
Files that contain common components can be reused in this way.
"""

# Create a base.html page that only contains shared components to be reused across multiple pages

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{{url_for('static', filename='format.css')}}" />
    <title>{% block title %} <!-- Placeholder for Title -->{% endblock %} - Jinja Demo </title>

    {% block head %}
    <!-- Placeholder for Page Content -->
    { endblock }
</head>
<body>
    <div id="header"> JINJA DEMO </div>
    <div id="content">
        {% block content %}
        <!-- Placeholder for Page Content -->
        {% endblock %}
    </div>
    <div id="footer"> Copyright © 2019 All Rights Reserved </div>
</body>
</html>

# the placeholders above are syntax for blocks in jinja

"""Blocks:
In Jinja, blocks are used as placeholders as well as replacements.  In the parent template, these blocks are used as placeholders.
In child template, they are used as replacements.

In the above example, base.html is the parent template.  A child template would replace the placeholders
"""

# Example implementation

# base.html

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{{url_for('static', filename='format.css')}}" />
    
  <title>{% block title %}<!-- Placeholder for Title -->{% endblock %} - Jinja Demo</title>
   
    {% block head %} 
    <!-- Placeholder for Other Imports -->
    {% endblock %}
    
</head>
<body>
    <div id="header"> JINJA DEMO </div>
    <div id="content">
        {% block content %}
        <!-- Placeholder for Page Content -->
        {% endblock %}
    </div>
    <div id="footer"> Copyright © 2019 All Rights Reserved </div>
</body>
</html>

# home.html
{% extends "base.html" %}

<!-- Replacement for Title -->
{% block title %}
Home Page
{% endblock %}

<!-- Replacement for Content -->
{% block content %}
<h1>Home Page</h1>
<p>Welcome to the Jinja2 Demo.</p>
{% endblock %}

# about.html
{% extends "base.html" %}

<!-- Replacement for Title -->
{% block title %}
About Page
{% endblock %}

<!-- Replacement for Content -->
{% block content %}
<h1>About Page</h1>
<p>In this lesson we are learning about Template Inheritance</p>  
{% endblock %}

# app.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

""" Notice the child template use {%extends "base.html" %} to inherit
from base.html
"""


"""Problem Statement:
In real-world application, we want data to be dynamic.
Let's render the data present in the application onto the templates.
You apre provided a list of dictionaries, called pets, containing info about pets.
Render this data in the form of a table using a for loop in the home.html template
"""

# app.py
"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html")


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Home - Paws Rescue Center</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
</head>
<body>
  <h1 id = "title"><center>Paws Rescue Center 🐾</center></h1>
  <table>
    <tr>
      <th>Image</th>
      <th>Name</th>
      <th>Age</th>
      <th>Bio</th>
    </tr>
  </table>
</body>
</html>

# app.py implemented solution
"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def homepage():
    """View function for Home Page."""
    # return pets dictionary from the homepage view.
    # this will enable us to access this variable in the home.html template - neato!
    return render_template("home.html", pets = pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# implemented solution to home.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Home - Paws Rescue Center</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
</head>
<body>
  <h1 id = "title"><center>Paws Rescue Center 🐾</center></h1>
  <table>
    <tr>
      <th>Image</th>
      <th>Name</th>
      <th>Age</th>
      <th>Bio</th>
    </tr>
    # add a loop for pet in pets
    # this will traverse through the pets dictionary
    {% for pet in pets %}

    # add a new table row in the loop that renders all columns of a single pet.
    # we used the Python syntax {{ }} to get values from the dictionary
    # last part is tricky.  Get the filename for the image associated with each pet by using the pet["id"]
    # variable and convert it into a string using string filter in Jinja.
    # Then, this id was appended to the string '.jpg' to create the complete filename
    <tr>
      <td><img src= "{{url_for('static', filename = pet['static', filename = pet["id"]|string+",jpg)}}" height = "100"></td>
      <td>{{ pet["name"] }}</td>
      <td>{{ pet["age"] }}</td>
      <td>{{ pet["bio"] }}</td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>

# Project Challenge: Create Dynamic Route for Pet Details

"""
Create a new route in the app to the URL: "/details/pet_id" where pet_id is a valid pet's id
It should return a web page containing all info regarding that pet
Update the homepage such that clicking the pet's image redirects to it's details page
"""

# app.py

"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html", pets = pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")


# create a route associated with this view that is a variable rule, and int is a converter
@app.route("/details/<int:pet_id>")

# create a new function pet_details

def pet_details(pet_id):
    # view function showing details of each pet
    # search the list of dictionaries for the dictionary containing id ==pet_id
        pet = next((pet for pet in pets if pet["id"] ==pet_id), None)
    # if the pet does not exist, call the abort() function with a 404 response and escription
    if pet is None:
        abort(404, description="no Pet was found with that given ID")
    # if the pet is found, return the dictionary with details.html template
    return render_template("details.html", pet = pet)


# create a new route for pet_id
@app.route("/details/pet_id")
def pet_id():
    return render_template("pet_id.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# details.html doesn't exist earlier.  let's add the file and the following contents
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    # add the pet name into the title
    <title>{{pet["name"]}}'s Details - Paws Rescue Center</title>
    link rel="stylesheet" href="{{url_for('static', filename="style.css")}} />
</head>
<body style="margin:2%"> 
    <div style="float:left; border-style:double;">

        <img src = "{{url_for('static', filename=pet["id"]|string+".jpg)}}" height = "350" >
    </div> 
    <div style="float:left; margin:10px;">
    <h1 class="title">{{pet["name"] }}</h1>
    # we added columns with name age and bio
    <p><b>Age: &nbsp; </b> {{pet["age"]}}</p>
    <p><b>Bio: &nbsp;</b> {{pet["bio"]}}</p>
    </div>
</body>
</html>


# Project Challenge: Template Inheritance
"""
- Create a parent template and inherit all other templates from it
- Make sure that all the redundant content is contained by the parent
- Make changes to child templates so that they can replace the placeholders present in parent template

"""

# given app.py

"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template, abort
app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# given home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Home - Paws Rescue Center</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
</head>
<body>
  <h1 id = "title"><center>Paws Rescue Center 🐾</center></h1>
  <table>
    <tr>
      <th>Image</th>
      <th>Name</th>
      <th>Age</th>
      <th>Bio</th>
    </tr>
    {% for pet in pets %}
    <tr>
        <td >
            <a href="{{url_for('pet_details', pet_id = pet['id'])}}">
                <img src= "{{url_for('static', filename = pet["id"]|string+".jpg")}}" height="100" >
            </a>
        </td>
        <td>{{ pet["name"] }}</td>
        <td>{{ pet["age"] }}</td>
        <td>{{ pet["bio"] }}</td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>

# given about.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>About - Paws Rescue Center</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
</head>
<body>  
    <h1 class="title">About Us:</h1>
    <p>
        We are a non-profit organization working as an animal rescue.
        We aim to help you connect with purrfect furbaby for you!
        The animals you find at our website are rescued and rehabilitated animals.
        Our mission is to promote the ideology of "Adopt, don't Shop"!
    </p>
</body>
</html>

# given details.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{pet["name"]}}'s Details - Paws Rescue Center</title>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
</head>
<body style="margin:2%"> 
    <div style="float:left; border-style:double;">
        <img src= "{{url_for('static', filename = pet["id"]|string+".jpg")}}" height="350" >
    </div> 
    <div style="float:left; margin:10px;">
        <h1 class="title">{{ pet["name"] }}</h1>
        <p><b>Age: &nbsp;</b> {{pet["age"]}}</p>
        <p><b>Bio: &nbsp;</b> {{pet["bio"]}}</p>
    </div>
</body>
</html>

# create a base.html and put all the recycleable components in there

# base.html
# we have a few basic things to include in the base.html
# reference the style.css or format.css sheet that's referenced throughout
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
    
    # create a title line that can be used for all of them
  <title>{% block title %} {% endblock %} Paws Rescue Center</title>
   
    {% block head %} 
    <!-- Placeholder for Other Imports -->
    {% endblock %}
    
</head>
<body>
    <div id="header"> JINJA DEMO </div>
    <div id="content">
        {% block content %}
        <!-- Placeholder for Page Content -->
        {% endblock %}
    </div>
</body>
</html>

# home.html updated
{% extends "base.html" %}

{% block title %} Home {% endblock %}

{% block heading %}
<center>Paws Rescue Center 🐾</center>
{% endblock %}

{% block content%}
  <table>
    <tr>
      <th>Image</th>
      <th>Name</th>
      <th>Age</th>
      <th>Bio</th>
    </tr>
    {% for pet in pets %}
    <tr>
        <td >
            <a href="{{url_for('pet_details', pet_id = pet['id'])}}">
                <img src= "{{url_for('static', filename = pet["id"]|string+".jpg")}}" height="100" >
            </a>
        </td>
        <td>{{ pet["name"] }}</td>
        <td>{{ pet["age"] }}</td>
        <td>{{ pet["bio"] }}</td>
    </tr>
    {% endfor %}
  </table>
{% endblock %}

"""Home/about/details.html updates:
child templates had replaced the contents in their respective blocks
it is not necessary to replace all placeholder blocks

"""
