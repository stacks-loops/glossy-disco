# from flask import render_template, request, jsonify
# from .app import app, db
# from .models import Workout, Step

# @app.route('/')
# def index():
#     message = "Hello from the otherside"
#     return render_template('index.html', text_content=message)

# @app.route('/add-workout', methods=['POST'])
# def add_workout():
#     data = request.get_json()

#     workout = Workout(title=data['title'])

#     for step in data['steps']:
#         new_step = Step(
#             exercise_name=step['exerciseName'],
#             description=step['description'], 
#             sets=step['sets'],
#             reps=step['reps'],
#             interval_type=step['intervalType'],
#             interval_value=step['intervalValue'],
#             workout=workout
#         )
#         db.session.add(new_step)

#     db.session.add(workout) 
#     db.session.commit()

#     return jsonify({'message': 'Workout created successfully!'}), 201 