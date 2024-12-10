from flask import Blueprint, request, jsonify
from datetime import timedelta
from .models import db, Employee, PTOEntry, User
from .extensions import jwt_required, create_access_token, get_jwt_identity, get_jwt

blacklisted_tokens = set()

main = Blueprint('main', __name__)

@main.route('/api/v1/test_route')
def your_function(): 
    return "Hello, World!"

@main.route('/api/v1/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})

@main.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        access_token = create_access_token(identity=user.username, expires_delta=timedelta(minutes=60))
        return jsonify({'access_token': access_token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@main.route('/api/v1/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklisted_tokens.add(jti)
    return jsonify({'message': 'Logged out successfully!'})

@main.route('/api/v1/employees', methods=['GET'])
@jwt_required()
def get_employees():
    employees = Employee.query.all()
    ret = [employee.serialize_employee() for employee in employees]
    return jsonify(ret)

@main.route('/api/v1/employees', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.get_json()
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully!'})

@main.route('/api/v1/employees/<employee_id>', methods=['PUT'])
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

@main.route('/api/v1/employees/<employee_id>', methods=['DELETE'])
@jwt_required()
def remove_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee removed successfully!'})
    else:
        return jsonify({'message': 'Employee not found'}), 404

@main.route('/api/v1/pto', methods=['GET'])
@jwt_required()
def get_pto_entries():
    ptos = PTOEntry.query.all()
    ret = [pto.serialize_pto_entry() for pto in ptos]
    return jsonify(ret)

@main.route('/api/v1/pto', methods=['POST'])
@jwt_required()
def add_pto_entry():
    data = request.get_json()
    employee = Employee.query.get_or_404(data["employee_id"])
    if employee:
        new_pto_entry = PTOEntry(hours=data['hours'], employee_id=employee.id)
        db.session.add(new_pto_entry)
        employee.hours_balance -= float(data['hours'])
        db.session.commit()
        return jsonify({'message': 'PTO entry added successfully!'})
    else:
        return jsonify({'message': 'Employee not found'}), 404

@main.route('/api/v1/pto/<pto_id>', methods=['DELETE'])
@jwt_required()
def remove_pto_entry(pto_id):
    pto = PTOEntry.query.get_or_404(pto_id)
    if pto:
        pto.employee.hours_balance += pto.hours
        db.session.delete(pto)
        db.session.commit()
        return jsonify({'message': 'PTO entry removed successfully!'})
    else:
        return jsonify({'message': 'Employee not found'}), 404
