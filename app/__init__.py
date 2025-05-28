from flask import Flask
from flask_restx import Api
from config.db import get_db, close_db

# Controller Part
from api.controllers.customer_controller import customers


def create_app(): 
    app = Flask(__name__)
    api = Api(
        app,
        title="Research Project",
        description="New Initialize Backend Project in Sales Customers", 
        version="1.0"
    )

    app.config.from_object("config.Config")
    app.teardown_appcontext(close_db)

    # Namespace API
    api.add_namespace()

    return app