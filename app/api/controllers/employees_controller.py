from flask_restx import Namespace, fields, Resource
from flask import jsonify, request 

from ..services.employee.employees import (
    get_list_employees, 
    get_employee_details, 
    update_employee, 
)

from ..models.employees_model import (
    api, 
    get_list_employee_parameter, 
    get_detail_employee_parameter,
    update_employee_response_parameter, 
)


@api.route("")
class Employees(Resource): 

    @api.response(200, "Return Employee List", get_list_employee_parameter)
    def get(self): 
        response_data = get_list_employees()
        return jsonify(
            {
                "code": "200", 
                "message": "Data Status OK", 
                "data": response_data
            }
        )
    
    @api.route("/<int:employeeid>")
    class EmployeeDetails(Resource): 
        @api.response(200, "Return Employee Details", get_detail_employee_parameter)
        def get(self, employeeid): 
            result = get_employee_details(employeeid)
            return jsonify({
                "code": "200", 
                "message": "Data Status Ok", 
                "data": result
            })
        
        @api.expect(update_employee_response_parameter)
        def put(self, employeeid): 
            updateEmployee = update_employee(employeeid, request.get_json())
            return jsonify({
                "code": "200", 
                "message": "Data Successfully updated", 
                "data": updateEmployee, 
            })
