from flask import Flask, render_template

'''
This code gets a basic web server up and running and makes
it respond with a home.html template, which will be served
to a browser when navigating to the URL "/".
'''

app = Flask(__name__)

@app.route("/")
def home():
    '''
    You connect the URL route "/" to the home()
    function by decorating it with @app.route("/"). A
    decorator is a function that takes another function
    and extends the behavior of the latter function
    without explicitly modifying it.
    '''

    return render_template("home.html")
    '''
    home() calls the Flask render_template() function to
    get the home.html file from the templates directory
    and return it to the browser.
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)