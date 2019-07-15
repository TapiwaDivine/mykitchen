# Kichen Directory
This is web application which vistors will be able to add recipes, edit recipes, update recipes and delete recipes. Vistors will also be create an account and login.
This web application can be inproved in many way but for now we have managed to put only the basic in place to be able to get the web application interactive. Users
can show their approval for the recipes by liking and also we set a views tracker that increments at each visit to a recipe. This project has been an eye openner in understanding
python, flask, pymongo, and mongodb. 
## Content Table

1. [UX](#UX)
2. [Features](#Features)
    +   1. [Existing Features](#existing-features)
    +   2. [Features Left to Implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
    +   1. [Content](#content)
    +   2. [Media](#media)
    +   3. [Acknowledgements](#acknowledgements)


## UX
1. This  Web aplication is a users driven web app were users populate the webisite with recipes and share or store their recipes. Users will be able to do a CRUD though we didnt get deep into the knit grities this aspect we set up a basic CRUD and a Basic Sing up and Login. The user will be a able to see the most popuplar recipe or recently. Visitors will also be able to view recipes in their categories and we have eight categories. 
2. Colour: The theme colour of this project is Red and white images from showcase, footer and recipes also contribute in beautifiying this web app.
3. Pages : This web app has about 16 pages which can be openned through either navbar, categories and viewing recipes
4. Mock up: I did a sketch on paper then did this mock up on [figma.com](https://www.figma.com/file/WE8kATa6uxCL4YJVQJzjuRze/MyKitchen-Mockup?node-id=0%3A1, i also used a logo made  at freelogodesign.com) and also the database design was done on a piece of paper
![Frontend paper sketch](https://res.cloudinary.com/deesjttvu/image/upload/v1562672577/IMG_20190709_114340_amplce.jpg)
![backend paper sketch](https://res.cloudinary.com/deesjttvu/image/upload/v1562672604/IMG_20190518_111112_vmagej.jpg)

## Features

### Existing Features
* This web app has 16 pages and the database supporting it has 24 documents
* There are 5 key sections on this webapp:
    - landing page/ home page
    - Recipes page
    - Add Recipe page
    - Signup page
    - Login page

- Common features
    * Each section has a responsive design and navigation bar with a logo on the which i was created through freelogodesign.com (is also linked to home page) and other menu items to the right and to the left side of the logo that take you to each page accordingly.
    * At the bottom there is a footer which include copyright and social media icons.
    * Recipes Cards display the Recipe Image, Recipe Name, Basic descrption of the recipe, recipe author and views, likes, cooking time and number of people the recipe serves
    * Add Recipe forms and Edit Recipe forms these provide fields that will be set i the database 

- Landing page/Home page
    * The home page has a hero image with a call to action and a signup button(inspired by bigoven.com)
    * I also has a section form the popular recipes with most views which is limited to 6 recipes in 3x2 rows. this i was insipred by(https://tajinny.com/) though i added my own feel
    * the page closes with a hero footer which has contacts and a brief about us
    
- Recipes page 
    * has a Recipe Of the Month with is elected by most likes
    * And has categories column to view recipes by category
    * this page also has a section for recent recipes structed by date created

- View Recipe
    * The view recipe is access when user clicks a red button with 3 dots in each recipe
    * View recipe gives all the the details on the recipe collected in the collection
    * there is also a thumb up handle that collects likes
    * at th bottom the is an edit and a delete button which are all functioning well

- Signup and Login(YouTube channels Pretty Printed and Corey Schafer, helped understanding and implematation of these 2) 
    * signup page offer a signup form for user and password encryption with bcrypt when submitted and also a link to the login page
    * login provides a basic form which users login and using an email or password

### Features Left to Implement

- Features Left to Implement to implement include a user dashboard when they login and controls over who can edit a recipe or delete it
- Also in the recipe views we cold use videos in steady of images
- Also when a user login the display of the user image  and a logout button could make a difference
- To note that the adding of images onthe recipe can be changed from using a image link to a image file
- also the storage of sessions for users and error handling
- I also think there should be a control around the word and things people enter to avoid abuse of web app
- Also to use environments variable access database


## Technologies Used
1. In this project i used:
    * python framework Flask
    * dnspython
    * pymongo
    * mongodb
    * jinja2
    * flask-bcrypt 
    * wt-forms
    * Heroku
2. This project was styled with Bootstrap, fontawesome and Css
3. I used [mongo atlas](mongodb.com) as the server
4. I also used [cloudinary](cloudinary.com) to store all pictures and render them links
5. Figma was my mockup platform of choice it worked fantastic form me.

## Testing
- All code were validated through:
    - [W3C Mark-up Validation Service](https://validator.w3.org/)
    - [W3C CSS Validation Service](http://www.css-validator.org/)
- Add Recipe And Edit Recipe forms
    - I tested both form and forms are functioning well and have a required element to make sure that no field will be empty
- Login Form and Signup
    - both form are tested for with empty submition which both of which will request user to enter information in required fieldset
    - both forms require valid emails as they will not accept invalid email
    - both form have feedback on submission if the submition is successful
- Mobile Responsive
    - This web-app is mostly responsive in most screens i have tested it on Iphone X, Huawei Psmart2019,Windows Chrome browser and Opera browser
    - To note is that there is bug on the signup and login nav link as they are unclickable on the mobile screens
- Testing on this project was done manually using developer toools to test the website
- I also openned each page to check and see if there are any bug or frontend errors.

## Deployment
- This project was created in 2 environments Cloud9 ide and AWS cloud9 both environments pushed code to github and heroku respectively
- [github](https://github.com/TapiwaDivine/mykitchen)
- [heroku](https://mykitchen07.herokuapp.com/)

## Credits
- YouTube Channels
    - Pretty Printed
    - Learn with Ali Hossain
    - Traversy Media
    - Corey Schafer
- Stack overflow
- Miguel Grinberg (Flask mega tutorial)
- Tutors at code institute
- My Mentor (Maranatha)
- Flask documentation
- Jinja2 Documentation
- mdbootstrap.com
- getboostrap.com
- Materializecss.com

### Content
- getboostrap.com were i accessed code for all the bootstrap in this project
- Materializecss.com were all the other styles thata re not boostrap came from
- Stack overflow were most of my solutions came from
- Code Institute most of the layout in the project were from the lessons source
- W3schools.com - helpful in this project also
- mdbootstrap - i used it to set up the base.html footer
- Corey Schafer - mostly his video on YouTube helped to set up the forms for login and signup
- Learn with Ali Hossain - i learned a different way of styling a navbar and putting the logo on the center
- Miguel Grinberg (Flask mega tutorial), Pretty Printed, Traversy Media, tutors at code institute and  Maranatha all the mentioned helped me understand concepts that apply not only in pyhton by to manny other languages

### Media

- Most pictures used were all download at random googles search in images of the particular recipe

### Acknowledgements
- I drew insipiration from bigoven.com and tajinny.com the 2 sites that had the most influence to the web app
- I would also wanted to acknowledge the work done by the forementioned at the credits section to whom the biggest percentage of the codein the project has been influenced from or brought understanding to the needs of this project
- Special mention to Code institute Tutors and my mentor, God Bless 
