from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy  # Import for database 


from glossy_disco.models import Workout, Step

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

#import routes
from .backend.routes import *

if __name__ == '__main__': 
    app.run(debug=True) 