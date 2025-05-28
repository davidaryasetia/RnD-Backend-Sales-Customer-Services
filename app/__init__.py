from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()
api = Api(title="My API", version="1.0", description="Flask-RESTX Example")

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    api.init_app(app)

    from .routes import ns_example
    api.add_namespace(ns_example)

    return app
