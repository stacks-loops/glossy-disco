from flask import Flask, request, jsonify
from config import ApplicationConfig
from models import db, Workout, Step
from routes import add_workout
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session

from flask_sqlalchemy import SQLAlchemy  # Import for database 
import ipdb

app = Flask(__name__)
app.config.from_object(ApplicationConfig)

server_session = Session(app)

db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

api = Api(app)

CORS(app, origins=['http://localhost:5173'], supports_credentials=True)

if __name__ == '__main__': 
    app.run(debug=True) 