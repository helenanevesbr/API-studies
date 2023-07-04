from flask import render_template
import config
'''
The config module provides the Connexion-flavored Flask app now
Therefore, you don’t create a new Flask app
'''
from models import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)
'''
To show the people data in the front end,
 you query the Person model to get all the data from the person
 table and pass it on to render_template()
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)