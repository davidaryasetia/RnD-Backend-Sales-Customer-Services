from flask import Flask, redirect
from flask_restx import Api
from config.db import close_db

from .api.controllers import customer_controller

app = Flask(__name__)

api_prefix = "/api/sales_management"

api = Api(
        app,
        title="RnD Project (Sales Customers Management Service)",
        description="New Initialize Backend Project With Flask with existing structure project", 
        version="1.0"
)

@app.route('/api/sales_management')
def redirecting(): 
    return redirect(api_prefix)

app.teardown_appcontext(close_db)

# Register Common API
api.add_namespace(customer_controller.api, path="/customers")
