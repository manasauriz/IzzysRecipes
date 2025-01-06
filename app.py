import json

from flask import Flask, render_template

with open("static/recipes.json") as file:
    recipes = json.load(file)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
def noodles(name):
    return render_template("recipe.html", name=name, data=recipes[name])