import os
from flask import Flask, render_template, redirect, request, url_for
# MongoDB for flask
from flask_pymongo import PyMongo
# This module allows you to create and parse ObjectIDs without a reference to the mongodb or bson modules.
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'extinction_rebellion'
app.config["MONGO_URI"] = os.getenv('mongodb+srv://new:1234@firstcluster-jvp2j.mongodb.net/test?retryWrites=true&w=majority', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def say_hello():
    return '123'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)