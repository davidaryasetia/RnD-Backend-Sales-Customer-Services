from flask_restx import Namespace, fields

api = Namespace(
    name="Customers Management", 
)


customer_detail = api.model(
    "CustomerList", 
    {
        "customerid": fields.String(required=True, description="Customer ID"), 
        "customername": fields.String(required=True, description="Customer Name"), 
        "contactname": fields.String(required=True, description="Contact Name"), 
        "address": fields.String(required=True, description="Address"), 
        "city": fields.String(required=True, description="City"), 
        "postalcode": fields.String(required=True, description="Postal Code"), 
        "country": fields.String(required=True, description="Country"), 
    }
)

get_list_customer_parameter = api.model("customer list parameter", {
    "code" : fields.String("200"), 
    "message" : fields.String("Data Successfull"), 
    "data" : fields.List(fields.Nested(customer_detail))
})


get_detail_customer_parameter = api.model("Customer detail parameter", {
    "code" : fields.String("200"), 
    "message" : fields.String("Data Successfull"),
    "data" : fields.Nested(customer_detail)
})

get_delete_customer_parameter = api.model("Customer delete parameter", {
    "code" : fields.String("200"), 
    "message": fields.String("Data Successfull Delete"), 
    "data": fields.Nested(api.model("Delete customer_id", {
        "customerid": fields.Integer(),  
    }))
})