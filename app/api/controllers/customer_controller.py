from flask_restx import Resource, Namespace, reqparse
from flask import jsonify, request

# Services
from ..services.customer.customers import (
    get_list_customers,
    delete_customer, 
)

# Models 
from ..models.customer_model import (
    api, 
    get_list_customer_parameter, 
    get_detail_customer_parameter,
    get_delete_customer_parameter, 
) 


@api.route("")
class Customers(Resource): 

    # List Customers Data 
    @api.response(200, "Return Customers List", get_list_customer_parameter )
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
        @api.response(200, "Return Customer Details", get_detail_customer_parameter)
        def get(self, customer_id): 
            result="On Progress"
            return jsonify({
                "code": "200", 
                "message": "Data Status Ok", 
                "data": result
            })
        
    @api.response(200, "Return Customer Delete", get_delete_customer_parameter)
    def delete(self, customer_id): 
        delete_customer(customer_id)
        return jsonify({
            "code": "200", 
            "message": "Customer Deleted Successfully", 
            "data" : {
                "customer_id": customer_id
            }
        })