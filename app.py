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
    return render_template('index.html',
                            recipes=mongo.db.recipes.find().limit(3))
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                            categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=recipe)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.tasks
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'title':request.form.get('title'),
        'description':request.form.get('description'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'cooking_time':request.form.get('cooking_time'),
        'serving':request.form.get('serving'),
        'author':request.form.get('author'),
        'category': request.form.get('category'),
        'country_of_origin': request.form.get('country_of_origin'),
        'allergens':request.form.get('allergens'),
        'likes':request.form.get('likes'),
        'views':request.form.get('views'),
        'picture': request.form.get('picture'),
        
    })


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
