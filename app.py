import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_bootstrap import Bootstrap
from bson.objectid import ObjectId

# app config

app = Flask(__name__)

# Mongo Config

app.config["MONGO_DBNAME"] = 'recipe_databases'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://localhost//')

mongo = PyMongo(app)


# display card on we website
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html",
                            recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                            categories=mongo.db.Categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
