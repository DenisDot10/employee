from datetime import datetime
from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    hire_date = db.Column(db.Date, default=datetime.utcnow)
    salary = db.Column(db.Float)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow) 