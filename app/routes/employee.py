from flask import Blueprint, request, jsonify
from ..models import db, Employee
from ..extensions import jwt_required

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees', methods=['GET'])
@jwt_required()
def get_employees():
    employees = Employee.query.all()
    ret = [employee.serialize_employee() for employee in employees]
    return jsonify(ret)

@employee_bp.route('/employees', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.get_json()
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully!'})

@employee_bp.route('/employees/<employee_id>', methods=['PUT'])
@jwt_required()
def update_pto_balance(employee_id):
    data = request.get_json()
    employee = Employee.query.get_or_404(employee_id)
    new_pto_balance = data['hours_balance']

    if new_pto_balance is not None:
        employee.hours_balance = new_pto_balance
        db.session.commit()
        return jsonify({'message': 'Employee PTO balance updated successfully'})
    else:
        return jsonify({'message': 'Invalid data provided'}), 400

@employee_bp.route('/employees/<employee_id>', methods=['DELETE'])
@jwt_required()
def remove_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee removed successfully!'})
    else:
        return jsonify({'message': 'Employee not found'}), 404
