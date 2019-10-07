import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
# MongoDB for flask
from flask_pymongo import PyMongo
# This module allows you to create and parse ObjectIDs without a reference to the mongodb or bson modules.
from bson.objectid import ObjectId
# module allowing to retrieve current date and time in UTC format
from datetime import datetime

app = Flask(__name__)
app.secret_key = "chonk"
app.config["MONGO_DBNAME"] = 'extinction_rebellion'
app.config["MONGO_URI"] = 'mongodb+srv://new:1234@firstcluster-jvp2j.mongodb.net/extinction_rebellion?retryWrites=true&w=majority'

mongo = PyMongo(app)

# landing page - displays all the records in the database
@app.route('/')
def get_records():
    return render_template("records.html", records=mongo.db.repo.find().sort("date_added", -1)) # sorts from newest records to oldest

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
    # requests form values and places them in the dictionary
    form_values = request.form.to_dict()
    # adds values for date time when the record is added...
    form_values["date_added"] = datetime.utcnow()
    # ... and a number of votes (default = 0)
    form_values["votes"] = int(0)
    # inserts new record taking values form the form on /add
    records.insert_one(form_values)
    flash('New entry added!')
    return redirect(url_for('get_records'))

# route for updating existing record to the database
@app.route('/update_record/<record_id>', methods=["POST"])
def update_record(record_id):
    records = mongo.db.repo
    # inserts new record taking values form the form on /edit
    records.update({'_id': ObjectId(record_id)},
        {'title': request.form.get('title'),
        'url': request.form.get('url'),
        'desc': request.form.get('desc'),
        'category': request.form.get('category')})
    flash('Entry updated!')
    return redirect(url_for('get_records'))

# view displaying categories available, together with their descriptions
@app.route('/categories')
def show_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())

@app.route('/categories/<category_name>')
def single_category(category_name):
    selected_category = mongo.db.categories.find_one({"category_name": category_name})
    records_from_category = mongo.db.repo.find({"category": category_name})
    return render_template("single_category.html", category=selected_category, records=records_from_category)

# view asking user for confirmation after pressing delete
@app.route('/delete/<record_id>')
def delete_record(record_id):
    selected_record = mongo.db.repo.find_one({"_id": ObjectId(record_id)})
    return render_template('delete.html', record=selected_record)

# view asking user for confirmation after pressing delete
@app.route('/record_deleted/<record_id>')
def deleted(record_id):
    selected_record = mongo.db.repo.find_one({"_id": ObjectId(record_id)})
    mongo.db.deleted.insert(selected_record)
    mongo.db.repo.remove(selected_record)
    flash('Entry deleted!')
    return redirect(url_for('get_records'))

# route for displaying login page
@app.route('/login', methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        given_username = request.form["username"]
        given_password = request.form["password"]
        # looks up if user exists in the database
        username_found = mongo.db.users.find_one({"login": given_username})
        if username_found:
           # compares passwords
           if given_password == username_found["password"]:
               session["username"] = request.form["username"]
           else:
               flash('Wrong password, try again!')
               return redirect(url_for('user_login'))
        else:
            flash('Wrong username or password')
            return redirect(url_for('user_login'))
        flash('You were just logged in')
    # if user is already logged in, they are redirected to main page
    if "username" in session:
        return redirect(url_for('get_records')) # ????????????????????????? think what to do with it
    return render_template("login.html")

@app.route('/logout')
def user_logout():
    # clears session entirely, removing cookie as well
    session.clear()
    flash('You were logged out!')
    return redirect(url_for('get_records'))

# voting fuction
# upvote...
@app.route('/upvote/<record_id>')
def upvote_now(record_id):
    mongo.db.repo.find_one_and_update(
        {'_id': ObjectId(record_id)},
        {'$inc': {'votes': 1}}
    )
    return render_template("thumb_up.html", record=mongo.db.repo.find_one({'_id': ObjectId(record_id)}))

# downvoting will probably be removed
# #... and downvote
# @app.route('/downvote/<record_id>')
# def downvote_now(record_id):
#     mongo.db.repo.find_one_and_update(
#         {'_id': ObjectId(record_id)},
#         {'$inc': {'votes': -1}}
#     )
#     return render_template("thumb_up.html", record=mongo.db.repo.find_one({'_id': ObjectId(record_id)}))



# sorting by...
# ...date added

def sorting_by_date():
    mongo.db.repo.find().sort([("date", -1), ("votes", -1)]) # newest first
    mongo.db.repo.find().sort([("date", 1), ("votes", -1)]) # oldest first

    return redirect(url_for('get_records'))

# ...votes
def sorting_by_votes():
    mongo.db.repo.find().sort([("votes", 1), ("date", -1)]) # top votes first

    return redirect(url_for('get_records'))

# if __name__ == '__main__':
#     app.run(host=os.environ.get('IP'),
#             port=int(os.environ.get('PORT')),
#             debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port='8000',
            debug=True)