from flask import Flask, request, jsonify
from config import ApplicationConfig
from models import db, Workout, Step
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session

from flask_sqlalchemy import SQLAlchemy  # Import for database 
import ipdb

from models import Workout, Step

app = Flask(__name__)
app.config.from_object(ApplicationConfig)

server_session = Session(app)

db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

api = Api(app)

CORS(app, origins=['http://localhost:5173'], supports_credentials=True)



@app.route('/add-workout', methods=['POST'])
def add_workout():
    data = request.get_json()

    workout = Workout(title=data['title'])

    for step in data['steps']:
        new_step = Step(
            exercise_name=step['exerciseName'],
            description=step['description'], 
            sets=step['sets'],
            reps=step['reps'],
            interval_type=step['intervalType'],
            interval_value=step['intervalValue'],
            workout=workout
        )
        db.session.add(new_step)

    db.session.add(workout) 
    db.session.commit()

    return jsonify({'message': 'Workout created successfully!'}), 201 

if __name__ == '__main__': 
    app.run(debug=True) 