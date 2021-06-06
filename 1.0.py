# the simplest flask application can be made using just app.py
# i named it 1, but imagine it was named app.py for now

# import the flask module
from flask import Flask

# make an object with the imported Flask module.  This object will be our WSGI application called app.
app = Flask(__name__)
# run the application.  run does have some optional parameters, but we won't use any here
app.run()

# create a view function.  Tell the application to show something as output in the browser window.


def hello():
    return "Hello World!"

# tell the flask app when to call the view function hello().  We create a url route using route()


@app.route("/")
def hello():
    return "Hello World!!"


# not 100% sure about this next block.  It iniatilizes the app, and runs it setting the parameters of debug as well as the host and port
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
