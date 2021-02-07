from blog import app
from flask import render_template

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatti")
def contatti():
    return render_template("contatti.html")


@app.route("/mattia")
def mattia():
    return render_template("mattia.html")
