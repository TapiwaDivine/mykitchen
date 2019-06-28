import os
from dns import resolver
from flask import Flask, render_template, redirect, request, url_for, flash, session
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
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb+srv://localhost//")
app.config["SECRET_KEY"] = "190d61e8a37037e29228129682b22ea2"

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# class User(mongo.db.Model):
#    username = mongo.db.user_profile
    

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
    newrecipes = recipe.find().sort('date_created', pymongo.DESCENDING)
    return render_template('get_recipes.html', recipes=newrecipes)


# function to view and open the recipe
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    recipe_views = mongo.db.recipes   
    recipe_views.update({'_id': ObjectId(recipe_id)},
    { '$inc': {'views': 1}})
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
    recipes = mongo.db.recipes
    recipes.insert_one(form_data)
    return redirect(url_for('home'))
    
# creating function to editing recipes on the web app
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                            categories=all_categories)
                            
                            
# update function to post recipe after it was edited
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
        'picture': request.form.get('picture')
    })
    return redirect(url_for('home'))


# function to delete recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))



# function to insert recipe in the database
@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        form_data = form.data
        form_data['password'] = bcrypt.generate_password_hash(str(form.password.data).encode('utf-8'))
    
        users = mongo.db.users
        users.insert_one(form_data)
        session['Welcome {}'] = True
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Register', form=form)

# function to login users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = mongo.db.users.find_one(form.email.data)
            if user:
                if bcrypt.check_password_hash(user ['password'], form.password.data):
                    login_user(user)
                    session['logged_in'] = True
                    flash('You have been logged in!', 'success')
                    return redirect(url_for('home'))
            
            if user is None:
                flash('Login Unsuccessful. Please check your login details', 'danger')
                return render_template('login.html')
    
    return render_template('login.html', title='login', form=form)
    
@app.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


