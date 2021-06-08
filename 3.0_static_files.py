# Let's learn about hosting static files present in our flask app


"""
Static files(assets) are files that the server sends to the clients 'as-it-is' without any intervention.
Examples include: CSS files, background images, JavaScript files that are sent without modification
"""

"""Steps to serve Static files
- Create a \static directory
    -The same file structure strategies that applyh to templates also apply here.
- Create a URL for static files
    - We do not use views for static files, so a separate URL must be created.
    - Use the url_for() function
        - This function is used to build a URL for a certain endpoint.  We can use it to build
        URLs for view functions as well.  It takes the name of any associated variables as arguments
        url_for('view_function_name', variable_name = 'value_of_variable')
        The url_for function always returns an absolute URL for the endpoint.  Thus, we call it anywhere in the project and we will not have issues with relative paths
        If we end up changing the path for an endpoint or the route for a view, we do not have to change the hardcoded URL in the whole project
        Here's how to create the URL for a static file using a static endpoint: url_for('static', filename = 'name_of_file')_
"""

# Example application home.html file located in templates directory
<!DOCTYPE html >
<html >
   <head >
        <link rel = "stylesheet" href = "{{url_for('static', filename='borders.css')}}" / >
    </head >
    <body >
        <h1 > Home Page!</h1>
        <p > Welcome to the homepage for "How to Server Static Files" Demo!</p>
    </body >
</html >

""" Explanation:
We linked the css stylesheet with home.html using the <link> tag.
Instead of a relative path in the href attribute, we used url_for() to generate an absolute path for the static file
The double braces are part of Jinja's syntax.  Whatever Python variable or function call we place inside them is rendered in the template when rendered on the client-side
"""
