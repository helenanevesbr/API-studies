from flask import render_template # Remove: import Flask
from werkzeug import JSONEncoder
import connexion

app = connexion.App(__name__, specification_dir="./")
#This tells Connexion which directory to look in for its configuration file
app.add_api("swagger.yml")
#To connect the OpenAPI configuration file (swagger.yml) with your Flask app

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)