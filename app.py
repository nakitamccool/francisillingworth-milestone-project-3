import os
from flask import Flask , render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


db_password = os.environ.get('DB_PASSWORD')

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_project'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-aogax.mongodb.net/recipe_project?retryWrites=true&w=majority'

mongo = PyMongo(app) 

@app.route('/')




@app.route('/get.cuisines')
def get_cuisines():
    return render_template('cuisines.html', cuisine=mongo.db.cuisine.find())





@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipe.find())
    


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisine=mongo.db.cuisine.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipe
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = mongo.db.cuisine.find()
    return render_template('editrecipe.html', recipe = the_recipe, cuisine=all_cuisine)
    
    
    
@app.route('/update_recipe/<recipe_id>', methods = ["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipe
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name' : request.form.get('recipe_name'),
        'cuisine_type' : request.form.get('cuisine_type'),
        'author' : request.form.get('author'),
        'ingredients' : request.form.get('ingredients'),
        'method' : request.form.get('method'),
        'cook_time' : request.form.get('cook_time'),
    })
    return redirect(url_for('get_recipes'))

@app.route('/delete_task/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    



    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)