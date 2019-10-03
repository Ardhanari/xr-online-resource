import os
from flask import Flask, render_template, redirect, request, url_for
# MongoDB for flask
from flask_pymongo import PyMongo
# This module allows you to create and parse ObjectIDs without a reference to the mongodb or bson modules.
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")
app.config["MONGO_DBNAME"] = 'extinction_rebellion'
app.config["MONGO_URI"] = 'mongodb+srv://new:1234@firstcluster-jvp2j.mongodb.net/extinction_rebellion?retryWrites=true&w=majority'

mongo = PyMongo(app)

# landing page - displays all the records in the database 
@app.route('/')
def get_records():
    return render_template("records.html", records=mongo.db.repo.find())
    
# route allowing displaying one record based on its id 
# and possibly editing it (if user is logged in)
@app.route('/record/<record_id>')
def display_record(record_id): 
    # returns one record with id passed through
    selected_record = mongo.db.repo.find_one({"_id": ObjectId(record_id)})
    return render_template("single-record.html", record=selected_record)
    
# route to display form allowing to edit selected record    
@app.route('/edit/<record_id>')
def edit_record(record_id):
    selected_record = mongo.db.repo.find_one({"_id": ObjectId(record_id)})
    return render_template("edit-record.html", record=selected_record, categories=mongo.db.categories.find())
    
# route for displaying form that allows adding new link to the database
@app.route('/add')
def add_record():
    return render_template("add-record.html", categories = mongo.db.categories.find())
    
# route commiting new record to the database 
@app.route('/commit_record', methods=["POST"])
def commit_record():
    records = mongo.db.repo
    # inserts new record taking values form the form on /add 
    records.insert_one(request.form.to_dict())
    return redirect(url_for('get_records'))
    

# view displaying categories available, together with their descriptions
@app.route('/categories')
def show_categories():
    return render_template("categories.html")
    
# route for displaying login page
@app.route('/login')
def user_login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)