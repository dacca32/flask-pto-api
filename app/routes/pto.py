from flask import Blueprint, request, jsonify
from ..models import db, PTOEntry, Employee
from ..extensions import jwt_required

pto_bp = Blueprint('pto', __name__)

@pto_bp.route('/pto', methods=['GET'])
@jwt_required()
def get_pto_entries():
    ptos = PTOEntry.query.all()
    ret = [pto.serialize_pto_entry() for pto in ptos]
    return jsonify(ret)

@pto_bp.route('/pto', methods=['POST'])
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

@pto_bp.route('/pto/<pto_id>', methods=['DELETE'])
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
