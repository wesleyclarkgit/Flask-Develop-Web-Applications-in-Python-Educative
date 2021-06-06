# let's learn how to create dynamic URL routes in our application

# in the last lesson we studied views and routes. In dynamic routing, the rule parameter is not a constant string, like '/educative'.
# instead it's a variable.


from flask import Flaskapp = Flask(__name__)
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    # home view for the website
    return "Welcome to the homepage!"


@app.route("/<my_name>")
def greetings(my_name):
    # this time the view function is created by the variable to greet the user
    return "Welcome " + my_name + "!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


"""
In this small application, we can observe that in the second view function
called greetings(), we used the variable rule: /<my_name>
and returned a greeting to the user.
The my_name variable was extracted from the url.  IT was then converted into a string and passed
to the function greetings() to be used.
"""

# Here's another example of dynamic routing


@app.route("/")
def home():
    return "welcome to the home page"


@app.route('/square/<int:number>')
def show_square(number):
    # view that shows the square of the number passed by the url
    return "Square of " + str(number) + " is: " + str(number * number)

# in this example, there's a view function show_square(), which uses a variable rule as well as a converter for the rule
