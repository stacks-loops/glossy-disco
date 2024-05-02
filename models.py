from .backend import db

class Workout(db.Model):
    id = db.Column(db.string, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    qr_code_data = db.Column(db.Text)
    steps = db.relationship('Step', backref='workout', lazy="True")

class Step(db.Model):
    id = db.Column(db.String, primary_key=True)
    exercise_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)  
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    interval_type = db.Column(db.String(20), nullable=False) 
    interval_value = db.Column(db.Integer, nullable=False) 
    workout_id = db.Column(db.String, db.ForeignKey('workout_id'), nullable=False) 