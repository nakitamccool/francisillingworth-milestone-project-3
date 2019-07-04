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
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipe.find())
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)