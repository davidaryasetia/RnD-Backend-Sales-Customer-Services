from flask import Flask
from flask_restx import Api
from config.db import close_db

from .api.controllers import customer_controller

app = Flask(__name__)

api = Api(
        app,
        title="Research Project",
        description="New Initialize Backend Project in Sales Customers", 
        version="1.0"
)

app.teardown_appcontext(close_db)

# Register Common API
api.add_namespace(customer_controller.api, path="/customers")