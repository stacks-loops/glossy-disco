from config import app




# from flask import Flask
# from .config import ApplicationConfig
# from .models import db
# from .routes import add_workout
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_restful import Api

# from flask_sqlalchemy import SQLAlchemy  # Import for database 

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(ApplicationConfig)

#     db.init_app(app)
#     return app

# app = create_app

# migrate = Migrate(app, db)

# api = Api(app)

# CORS(app, origins=['http://localhost:5173'], supports_credentials=True)

# if __name__ == '__main__': 
#     app.run(debug=True) 