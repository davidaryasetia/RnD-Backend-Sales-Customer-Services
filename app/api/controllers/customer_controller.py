from flask_restx import Resource, Namespace, reqparse
from flask import jsonify, request

# Services
from ..services.customer.customers import (
    get_list_customers,
    get_customer_details, 
    delete_customer, 
    update_customer, 
)

# Models 
from ..models.customer_model import (
    api, 
    get_list_customer_parameter, 
    get_detail_customer_parameter,
    delete_customer_parameter, 
    update_customer_response_parameter, 
    update_customer_request_parameter, 
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
            result = get_customer_details(customer_id)
            return jsonify({
                "code": "200", 
                "message": "Data Status Ok", 
                "data": result
            })
        
        @api.expect(update_customer_request_parameter)
        @api.response(200, "Return Customer update", update_customer_response_parameter)
        def put(self, customer_id): 
            update_customer(customer_id, request.get_json())
            return jsonify({
                "code": "200", 
                "message": "Data Successfully Updated", 
                "data": None
            })

        @api.response(200, "Return Customer Delete", delete_customer_parameter)
        def delete(self, customer_id): 
            delete_customer(customer_id)
            return jsonify({
                "code": "200", 
                "message": "Customer Deleted Successfully", 
                "data" : {
                    "customerid": customer_id
                }
            })