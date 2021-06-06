# let's build an animal resue site called 'Paws Rescue Center'

from flask import Flaskapp = Flask(__name__)
from flask import Flask
import flask
app = Flask(__name__)

# add a static view for homepage


@app.route("/")
def home():
    return "Paws Rescue Center 🐾"
# add a static view for about page


@app.route("/about")
def about():
    return "We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology \"adopt, don't hop\"! "


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0". port=3000)

    """
    Here's what we learned in this lesson.
    The "/' URL route was used to make a home page.  We just returned a string when viewing this route

    The about page was created using the /about route.  We created the about() function that returned a string when landing on the /about page
    """

# Question:  What should be the return statement of the show_cube() function in the application given below.


@app.route('/square/<int:number>')
def show_cube(number):
    # view that shows the cube of the number passed by URL


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# Answer:


@app.route('/square/<int:number>')
def show_cube(number):
    return"Cube of " + str(number) + " is: " + str(number*number*number)

# The number is an integer type variable because we used the int converter in the route.  Therefore, we will have to convert it into a string using str() before concatinating with another string
