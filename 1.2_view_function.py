# In flask, we create a function that acts as the view.  This is what it looked like in the previous lesson

@app.route("/")
def hello():
    return "Hello World!";

 """the route decorateor contains a few parameters
- rule: the rule represents the URL rule which is passed as a string to the decorator
- endpoint(not needed): The endpoint is the name of the view function which is bound to the URL route.  Flask assumes this parameter itself, and the developer does not need to specify it
- options(optional):  Options are an optional parameter, out of scope for now

Static routing
In static routing we specify a constant URL string as a rule to the route() decorator.
"""

from flask import Flask, render_template
app = Flask(__name__)

# here's the static url with route() decorator
@app.route("/")
# the home view corresponds with the / route.  When you open the URL or check the 'output' tab, this view will be called
def home():
    return "Welcome to the Hope Page!"

# here's another static route
@app.route("/educative")
# the learn view, corresponds with /educative route.  When you open the URL and append the "/educative" this view will be called
def learn():
    return "Happy Learning at Educative!"


if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0, port=3000")
