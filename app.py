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
app.config["MONGO_URI"] = "mongodb+srv://root:1Britney@myprojectcluster-iqnfp.mongodb.net/recipes_database?retryWrites=true&w=majority"
app.config["SECRET_KEY"] = os.urandom(24)

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
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
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
    brkrecipes = recipe.find({"category": "Breakfast"})
    return render_template('breakfast.html', recipes=brkrecipes)
    
@app.route('/brunch_recipes')
def brunch_recipes():
    recipe = mongo.db.recipes
    brnchrecipes = recipe.find({"category": "Brunch"})
    return render_template('brunch.html', recipes=brnchrecipes)

@app.route('/lunch_recipes')
def lunch_recipes():
    recipe = mongo.db.recipes
    lunchrecipes = recipe.find({"category": "Lunch"})
    return render_template('lunch.html', recipes=lunchrecipes)
    
@app.route('/dinner_recipes')
def dinner_recipes():
    recipe = mongo.db.recipes
    dinnerrecipes = recipe.find({"category": "Dinner"})
    return render_template('dinner.html', recipes=dinnerrecipes)

@app.route('/dessert_recipes')
def dessert_recipes():
    recipe = mongo.db.recipes
    dessertrecipes = recipe.find({"category": "Dessert"})
    return render_template('dessert.html', recipes=dessertrecipes)

@app.route('/starter_recipes')
def starter_recipes():
    recipe = mongo.db.recipes
    starterrecipes = recipe.find({"category": "Starters"})
    return render_template('starters.html', recipes=starterrecipes)
    
@app.route('/sidedish_recipes')
def sidedish_recipes():
    recipe = mongo.db.recipes
    sidedishrecipes = recipe.find({"category": "Side Dish"})
    return render_template('sidedish.html', recipes=sidedishrecipes)
    
@app.route('/maindish_recipes')
def maindish_recipes():
    recipe = mongo.db.recipes
    maindishrecipes = recipe.find({"category": "Starters"})
    return render_template('starters.html', recipes=maindishrecipes)

@app.route('/snack_recipes')
def snack_recipes():
    recipe = mongo.db.recipes
    snackrecipes = recipe.find({"category": "Snack"})
    return render_template('snack.html', recipes=snackrecipes)   

@app.route('/recipeofthemth')
def recipeofthemth():
    recipe = mongo.db.recipes
    rotmrecipes = recipe.find().sort('views', pymongo.DESCENDING).limit(1)
    return render_template('get_recipes.html', recipes=rotmrecipes)

if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)