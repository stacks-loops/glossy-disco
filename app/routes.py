from flask import render_template
import datetime
from app import app

@app.route('/')
def index():
    message = "Hello from the otherside"
    return render_template('index.html', text_content=message)
