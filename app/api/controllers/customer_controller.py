from flask_restx import Resource, Namespace, reqparse
from flask import jsonify, request

# Services
from ..services.customer_service.get_list_customers import get_list_customers

# Models 
from ..models.customer_model import (
    api, 
    response_list_customers, 
) 


@api.route("")
class Customers(Resource): 

    # Customers Details 
    @api.response(200, "Return Customers List", response_list_customers )
    def get(self): 
        response_data = get_list_customers()
        return jsonify(
            {
                "code": "200",
                "message": "Data Status OK",
                "data": response_data,
            }
        )
    
    @api.route("/<int:customer_id>")
    class customer_details(Resource): 
        @api.response(200, "Return Customer Details")
        def get(self, customer_id): 
            result="On Progress"
            return jsonify({
                "code": "200", 
                "message": "Data Status Ok", 
                "data": result
            })