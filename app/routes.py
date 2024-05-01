from flask import render_template
import datetime
from app import app

@app.route('/')
def index():
    return ("Hello world welcome to glossy disco")
