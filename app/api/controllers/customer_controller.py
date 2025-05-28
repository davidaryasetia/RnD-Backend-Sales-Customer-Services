from flask_restx import Resource, Namespace, reqparse
from flask import jsonify, request

# Controllers


# Models 
from ..models.customer_model import (
    api, 
)

@api.route("")
class Customers(Resource): 

    # Customers Details 
    @api.response(200, "Return Customers List")
    def get(self): 
        response_data = "On Progress"
        return jsonify(
            {
                "code" : "200", 
                "message": "Data Status OK", 
                "data" : response_data,
            }
        )