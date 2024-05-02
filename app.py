from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Import for database 
from backend import db, routes  # Import your database object 

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/')  # Example route 
def hello_world():
    return 'Hello from Glossy Disco!'

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