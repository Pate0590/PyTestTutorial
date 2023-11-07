# Import the Flask class from the flask module
from flask import Flask

# Create a new instance of the Flask class. '__name__' is a built-in variable
# which evaluates to the name of the current module. This argument is needed
# so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger the function
# that follows it. In this case, the decorator indicates that the 'home'
# function gets called when there is a request for the root URL ('/').


@app.route('/')
def home():
    # The function returns the string "Hello, World!" to the web browser
    # or any other client that makes an HTTP request to the Flask server.
    return "Hello, World!"


# This conditional is only true if this script is being run directly
# and not being imported as a module. This is standard boilerplate in Python
# scripts which ensures that the server is started only when the script is
# executed directly.
if __name__ == '__main__':
    # This runs the application server. The 'debug=True' argument allows
    # possible Python errors to appear on the web page. This will help us
    # trace the errors.
    app.run(debug=True)
