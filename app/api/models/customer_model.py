from flask_restx import Namespace, fields

api = Namespace(
    name="Customers", 
)

response_list_customers = api.model(
    "CustomerList", 
    {
        "customer_id": fields.String(required=True, description="Customer ID"), 
        "customer_name": fields.String(required=True, description="Customer Name"), 
        "contact_name": fields.String(required=True, description="Contact Name"), 
        "address": fields.String(required=True, description="Address"), 
        "city": fields.String(required=True, description="City"), 
        "postal_code": fields.String(required=True, description="Postal Code"), 
        "country": fields.String(required=True, description="Country"), 
    }
)