import os
from flask import Flask, render_template, redirect, request, url_for, abort
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


# Home page and recipe card display
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',
                            recipes=mongo.db.recipes.find())

# viewing a clicked recipe
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    recipe_views = mongo.db.recipes   
    recipe_views.update({'_id': ObjectId(recipe_id)},
    { '$inc': {'views': 1}})
    return render_template('view_recipe.html', recipe=recipe)   
  
# route for add recipe page  
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                            categories=mongo.db.categories.find())
                            
# inserting recipe in the data base
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))
    
# creating route to editing recipes on the web app
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                            categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
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
        'picture': request.form.get('picture')
    })
    return redirect(url_for('home'))

@app.route('/update_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id: ObjectId(recipe_id)'})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
