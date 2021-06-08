"""Complete 2 tasks
You are provided with a style.css sheet, include it in both templates
Next add the images of pets in the column of the table
"""

# app.py

from flask.templating import render_template
from Flask import flask, reder_template
app = Flask(__name__)


@app.route("/")
def homepage():
    # view function of home page
    return render_template("home.html")


@app.route("/about")
def about():
    # view function for about page
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


# home.html

<!DOCTYPE html >
<html lang = "en" >
<head >
# add the style.css sheet using url_for
  <link rel = "stylesheet" href = "{{url_for('static', filename='style.css')}}" / >
      <meta charset = "utf-8" >
       <title > Home - Paws Rescue Center < /title >
</head >
<body >
  <h1 id = "title" > <center > Paws Rescue Center 🐾< /center > </h1 >
   <table >
      <tr >
       # add an image from the static directory
       <td > <link rel = "picture" href = "{{url_for('static', filename=1.jpg)}}" height = "100" > </td >
          <th > Image < /th >
           <th > Name < /th >
            <th > Age < /th >
            <th > Bio < /th >
        </tr >
        <tr >
        # add the static image more
          <td > <link rel = "picture" href = "{{url_for('static', filename='2.jpg')}}"height = "100" > </td >
           <td > Nelly < /td >
            <td > 5 weeks < /td >
            <td > I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles. < /td >
        </tr >
        <tr >
          <td > <link rel = "picture" href = "{{url_for('static', filename = '3.jpg')}}" height = "100" > </td >
           <td > Yuki < /td >
            <td > 8 months < /td >
            <td > I am a handsome gentle-cat. I like to dressup in bow ties. < /td >
        </tr >
        <tr >
        <td > <link rel = "picture" href = "{{url_for('static', filename = '4.jpg' )}} height="100" > </td >
          <td > Basker < /td >
           <td > 1 year < /td >
            <td > I love barking. But, I love my friends more. < /td >
        </tr >
        <tr >
          <td > <link rel = "picture" href = "({{url_for('static', filename = '5.jpg')}}" height = "100" > </td >
           <td > Mr. Furrkins < /td >
            <td > 5 years < /td >
            <td > Probably napping. < /td >
        </tr >
    </table >
</body >
</html >

# about.html
<!DOCTYPE html >
<html lang = "en" >
<head >
  <meta charset = "utf-8" >
   <title > About - Paws Rescue Center < /title >
    # add the static css stylesheet
    <td > <link rel = "picture" href = "{{url_for('static', filename=1.jpg)}}" height = "100" > </td >
</head >
<body >
  <h1 class = "title" > About Us: < /h1 >
   <p >
      We are a non-profit organization working as an animal rescue.
       We aim to help you connect with purrfect furbaby for you!
        The animals you find at our website are rescued and rehabilitated animals.
        Our mission is to promote the ideology of "Adopt, don't Shop"!
    </p >
</body >
</html >


""" Explanation:
We generated links for the static files using the url_for() method and added it to template files, enclosing them in {{}}
We provided the link for style.css by using: {{url_for('static', filename="style.acss")}}
"""

""" Questions:
What are static files or assets?
Static files are CSS, JS, images or siomilar files which ar sent to the client without server intervention

What is the url_for() function used for?
It is used to generate absolute URLs for endpoints.  We can use it to build URLs for view functions as well
"""

# Next let's work with Jinja to create dynamic templates
