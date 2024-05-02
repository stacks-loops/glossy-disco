from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'  # Adjust database name/location if needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but generally recommended
db = SQLAlchemy(app)