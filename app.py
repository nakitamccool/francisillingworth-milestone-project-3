import os
from flask import Flask , render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId




app = Flask(__name__)


db_password = os.getenv('DB_PASSWORD')

app.config["MONGO_DBNAME"] = 'recipe_project'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app) 

@app.route('/')



@app.route('/index')
def index():
    return render_template("index.html")


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

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    




@app.route('/get_cuisines')
def get_cuisines():
    return render_template('cuisines.html', cuisine=mongo.db.cuisine.find())
    

@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html', cuisine=mongo.db.cuisine.find_one({'_id':ObjectId(cuisine_id)}))
    

@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisine.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_type': request.form.get('cuisine_type')})
    return redirect(url_for('get_cuisines'))



@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html', cuisine=mongo.db.cuisine.find())


@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines=mongo.db.cuisine
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))



@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({'_id':ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))
    


@app.route('/add_cuisine_edit')
def add_cuisine_edit():
    return render_template('addcuisine-edit.html', cuisine=mongo.db.cuisine.find())


@app.route('/insert_cuisine_edit', methods=['POST'])
def insert_cuisine_edit():
    cuisines=mongo.db.cuisine
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisines'))



@app.route('/find_recipe')
def find_recipe():
    return render_template("findrecipe.html", cuisine=mongo.db.cuisine.find(), authors=mongo.db.recipe.find().distinct('author'))




@app.route('/filter_recipes', methods = ['POST','GET'])
def filter_recipes():
    recipes=mongo.db.recipe
    author=request.form.get('author')
    cuisine_type=request.form.get('cuisine_type')
    results=recipes.find({ "author": author})
    results_cuisine_type=recipes.find({ "cuisine_type":cuisine_type })
    number=recipes.count({ "cuisine_type":cuisine_type })
    return render_template("results.html", results = results, results_cuisine_type = results_cuisine_type)





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)