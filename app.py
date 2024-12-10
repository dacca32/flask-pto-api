from flask import Flask, request, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, 
    get_jwt_identity, get_jwt
)
import os

app = Flask(__name__)
# We do .replace here to account how Heroku serves their postgresql links
app.config['JWT_SECRET_KEY'] = 'qwertyuioplkjhgfdsazxcvbnm'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pto.db'
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_BLACKLIST_ENABLED'] = True 
app.config['FLASK_DEBUG'] = True # We set this to False for deployment
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database Models
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    hours_balance = db.Column(db.Float, default=0.0)
    pto_entries = db.relationship('PTOEntry', backref='employee', lazy=True, cascade="all, delete")
    def serialize_employee(self):
        return {"id": self.id,
                "name": self.name,
                "hours_balance": self.hours_balance,
                "pto_entries": [entry.serialize_pto_entry() for entry in self.pto_entries]}

class PTOEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Float, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    def serialize_pto_entry(self):
        return {"id": self.id,
                "hours": self.hours,
                "employee_id": self.employee_id}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

# Token Blacklist
blacklisted_tokens = set()

# Routes

@app.route('/api/v1/test_route')
def your_function(): 
    return "Hello, World!"

@app.route('/api/v1/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})

@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        access_token = create_access_token(identity=user.username, expires_delta=timedelta(minutes=60))
        return jsonify({'access_token':access_token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/v1/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklisted_tokens.add(jti)
    return jsonify({'message': 'Logged out successfully!'})

# Employee Endpoints
@app.route('/api/v1/employees', methods=['GET'])
@jwt_required()
def get_employees():
    employees = Employee.query.all()
    print('employeeeeeeees', employees)
    ret = []
    for employee in employees:
        ret.append(employee.serialize_employee())
    return jsonify(ret)

@app.route('/api/v1/employees', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.get_json()
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully!'})

# Update Employee PTO Balance Endpoint
@app.route('/api/v1/employees/<employee_id>', methods=['PUT'])
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


@app.route('/api/v1/employees/<employee_id>', methods=['DELETE'])
@jwt_required()
def remove_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee removed successfully!'})
    else:
        return jsonify({'message': 'Employee not found'}), 404

# PTO Entry Endpoints
@app.route('/api/v1/pto', methods=['GET'])
@jwt_required()
def get_pto_entries():
    ptos = PTOEntry.query.all()
    ret = []
    for pto in ptos:
        ret.append(pto.serialize_pto_entry())
    return jsonify(ret)

@app.route('/api/v1/pto', methods=['POST'])
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

@app.route('/api/v1/pto/<pto_id>', methods=['DELETE'])
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