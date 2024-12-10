from .extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    hours_balance = db.Column(db.Float, default=0.0)
    pto_entries = db.relationship('PTOEntry', backref='employee', lazy=True, cascade="all, delete")
    def serialize_employee(self):
        return {
            "id": self.id,
            "name": self.name,
            "hours_balance": self.hours_balance,
            "pto_entries": [entry.serialize_pto_entry() for entry in self.pto_entries]
        }

class PTOEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Float, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    def serialize_pto_entry(self):
        return {
            "id": self.id,
            "hours": self.hours,
            "employee_id": self.employee_id
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
