import json

from flask import Flask, render_template

with open("static/recipes.json") as file:
    recipes = json.load(file)

app = Flask(__name__)

@app.route("/")
def index():
    data = []
    for recipe in recipes:
        temp = {}
        temp["name"] = recipe
        temp["full_name"] = recipes[recipe]["name"]
        temp["description"] = recipes[recipe]["description"]
        print(temp)
        data.append(temp)
    return render_template("index.html", data=data)

@app.route("/<name>")
def noodles(name):
    return render_template("recipe.html", name=name, data=recipes[name])