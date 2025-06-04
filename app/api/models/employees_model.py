from flask_restx import Namespace, fields 

api = Namespace(
    name = "Employees Management", 
)

employee_detail = api.model(
    "EmployeeList", 
    {
        "employeeid": fields.Integer(required=True, description="Employee ID"), 
        "firstName": fields.String(required=True, description="First Name"), 
        "lastName": fields.String(required=True, description="Last Name"), 
        "birthDate": fields.String(required=True, description="Birth Date"), 
        "photo": fields.String(required=True, description="Photo URL"), 
        "notes": fields.String(required=True, description="Notes") 
    }
)

employee_update = api.model(
    "EmployeeUpdate", 
    {
        "firstName": fields.String("FirstName"), 
        "lastName": fields.String("LastName"), 
        "birthDate": fields.String("BirthDate"), 
        "photo": fields.String("Photo"), 
        "notes": fields.String("Notes")
    }
)

get_list_employee_parameter = api.model("Employee List Paramter", {
    "code": fields.String("200"),
    "message": fields.String("Data Successfull List"),
    "data": fields.List(fields.Nested(employee_detail))
})

get_detail_employee_parameter = api.model("Employee Detial Parameter", {
    "code": fields.String("200"), 
    "message": fields.String("Data Successfull Detail"), 
    "data": fields.Nested(employee_detail)
})

update_employee_response_parameter = api.model("Employee Update Parameter", {
    "code": fields.String("200"), 
    "message": fields.String("Data Successfully Updated"), 
    "data": fields.Nested(employee_detail)
})