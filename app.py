import os
import flask
from dns import resolver
from flask import Flask, render_template, redirect, request, url_for, flash, session, abort
from flask_pymongo import PyMongo, pymongo
from pymongo import MongoClient
from flask_bootstrap import Bootstrap
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import LoginManager, login_user, login_required, logout_user, current_user



# app config

app = Flask(__name__)


# Mongo Config

app.config["MONGO_DBNAME"] = "recipes_database"
app.config["MONGO_URI"] = "mongodb+srv://root:root@myprojectcluster-iqnfp.mongodb.net/recipes_database?retryWrites=true&w=majority"
app.config["SECRET_KEY"] = os.urandom(24)

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


# function to display home page and recent recipe card display
@app.route('/')
@app.route('/home')
def home():
    recipe = mongo.db.recipes
    poprecipes = recipe.find().sort('views', pymongo.DESCENDING).limit(6)
    return render_template('index.html', recipes=poprecipes)
    
    
                            
# function to open recipes page
@app.route('/get_recipes')
def get_recipes():
    recipe = mongo.db.recipes
    newrecipes = recipe.find().sort('date_created', pymongo.ASCENDING).limit(6)
    rotmrecipes = recipe.find().sort('likes', pymongo.DESCENDING).limit(1)
    return render_template('get_recipes.html', recipes=newrecipes, rotmrecipes=rotmrecipes)
    
    

# function to view and open the recipe
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    recipe_views = mongo.db.recipes   
    recipe_views.update({'_id': ObjectId(recipe_id)}, { '$inc': {'views': 1}})
    return render_template('view_recipe.html', recipe=recipe)


# function to open add recipe page and link the categories select  
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                            categories=mongo.db.categories.find())
                            
    
                            
# function to insert recipe in the database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    form_data = request.form.to_dict()
    form_data['datecreated'] = datetime.utcnow()
    form_data['likes'] = 0
    form_data['views'] = 0
    recipes = mongo.db.recipes
    if recipes.insert_one(form_data):
        flash('Submitted','success')
        return redirect(url_for('home'))
    return abort(500)
    
    
    
# creating function to editing recipes on the web app
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                            categories=all_categories)
                            
    
                            
# update function to post recipe after it is edited
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {'$set':{
            'title':request.form.get('title'),
            'description':request.form.get('description'),
            'ingredients': request.form.get('ingredients'),
            'method': request.form.get('method'),
            'cooking_time':request.form.get('cooking_time'),
            'serving':request.form.get('serving'),
            'author':request.form.get('author'),
            'category_name': request.form.get('category_name'),
            'country_of_origin': request.form.get('country_of_origin'),
            'picture': request.form.get('picture')
    }})
    flash('Update successful', 'success')
    return redirect(url_for('get_recipes'))

# function to delete recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    if mongo.db.recipes.remove({'_id': ObjectId(recipe_id)}):
        flash('Deleted','success')
        return redirect(url_for('get_recipes'))
    return abort(404)

#function for users to insert likes
@app.route('/like_recipe/<recipe_id>')
def like_recipe(recipe_id):
    likerecipes = mongo.db.recipes
    likerecipes.update({"_id": ObjectId(recipe_id)}, { '$inc': {'likes': 1}})
    return redirect(url_for('view_recipe', recipe_id=recipe_id))



# function to insert recipe in the database
@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        form_data = form.data
        form_data['password'] = bcrypt.generate_password_hash(str(form.password.data).encode('utf-8'))
    
        users = mongo.db.users
        if users.insert_one(form_data):
            flash('Registration successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Registration Failed!', 'warning')
            return render_template('signup.html', title='Register', form=form)
    return render_template('signup.html', title='Register', form=form)



# function to login users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({'email': form.email.data})
        if user and bcrypt.check_password_hash(user ['password'], form.password.data):
            session['user'] = user['username']
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
      
        if user is None:
            flash('Login Unsuccessful. Please check your login details', 'danger')
            return render_template('login.html', form=form)
    
    return render_template('login.html', title='login', form=form)



#Categories 
@app.route('/breakfast_recipes')
def breakfast_recipes():
    recipe = mongo.db.recipes
    brkrecipes = recipe.find({"category_name": "Breakfast"})
    return render_template('breakfast.html', recipes=brkrecipes)
    
@app.route('/brunch_recipes')
def brunch_recipes():
    recipe = mongo.db.recipes
    brnchrecipes = recipe.find({"category_name": "Brunch"})
    return render_template('brunch.html', recipes=brnchrecipes)

@app.route('/lunch_recipes')
def lunch_recipes():
    recipe = mongo.db.recipes
    lunchrecipes = recipe.find({"category_name": "Lunch"})
    return render_template('lunch.html', recipes=lunchrecipes)
    
@app.route('/dinner_recipes')
def dinner_recipes():
    recipe = mongo.db.recipes
    dinnerrecipes = recipe.find({"category_name": "Dinner"})
    return render_template('dinner.html', recipes=dinnerrecipes)

@app.route('/dessert_recipes')
def dessert_recipes():
    recipe = mongo.db.recipes
    dessertrecipes = recipe.find({"category_name": "Dessert"})
    return render_template('dessert.html', recipes=dessertrecipes)

@app.route('/starter_recipes')
def starter_recipes():
    recipe = mongo.db.recipes
    starterrecipes = recipe.find({"category_name": "Starters"})
    return render_template('starters.html', recipes=starterrecipes)
    
@app.route('/sidedish_recipes')
def sidedish_recipes():
    recipe = mongo.db.recipes
    sidedishrecipes = recipe.find({"category_name": "Side Dish"})
    return render_template('sidedish.html', recipes=sidedishrecipes)
    
@app.route('/snack_recipes')
def snack_recipes():
    recipe = mongo.db.recipes
    snackrecipes = recipe.find({"category_name": "Snack"})
    return render_template('snack.html', recipes=snackrecipes) 


if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
