from flask import render_template
import datetime
from app import app

@app.route('/')
def index():
    current_time = datetime.datetime.now()
    return render_template('index.html', time=current_time) 
