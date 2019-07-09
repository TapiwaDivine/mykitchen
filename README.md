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


## Features

### Existing Features
* This web app has 16 pages and the database supporting it has 24 documents
* the Logo on this web app was created through freelogodesign.com
* This web app is responsive and can be used in most screen
* On this web app all the pages have a footer with social media link and copy right section and a navbar that was created to have a logo on the center(YouTube channel Learning with Ali Hossain,7months ago) and (mdbootstrap.com)
* Then we also have a hero image on top of the homepage and on the footer as well. These i meant to beautify the home page(insipered by bigoven.com) and give user that anticipation to do around the site. We also have the render of recipes which is limited to 6. this i was insipred by(https://tajinny.com/) though i added my own feel
* We have recipe of the that is insiped by most likes to a recipe by users.
* We also render recent recipe in the recipe page and also th categories of recipes
* We also have a add recipe page which present users with a form to add recipes to the web app
* We also have the view recipe which can be access when user clicks a red button with 3 dots in each recipe. through this avenue user can either edit or delete their recipes.
* We also have the signup form and the login form ready use by users(YouTube channels Pretty Printed and Corey Schafer) helped understanding and implematation of these 2

### Features Left to Implement
- Features Left to Implement to implement include a user dashboard when they login and controls over who can edit a recipe or delete it
- Also in the recipe views we cold use videos in steady of images
- Also when a user login the display of the user image  and a logout button could make a difference
- To note that the adding of images onthe recipe can be changed from using a image link to a image file
- also the storage of sessions for users and error handling
- I also think there should be a control around the word and things people enter to avoid abuse of web app
- Also to use environments variable access database


## Technologies Used
1. In this project i used pyhon framework flask, pymongo, mongodb, jinja2, flask-bcrypt to bring together the front and the backend
2. This project was styled by Bootstrap and Materializecss taking different section each to come up with nice designs that will no conflict with each other
3. I used [mongo atlas](mongodb.com) as the server
4. I also used cloudinary.com to store all pictures and render them links
5. Figma was my mockup platform of choice it worked fantastic form me.

## Testing
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
