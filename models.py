# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Tenant(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    apartment_number = db.Column(db.String(10), nullable=False)
    check_in_date = db.Column(db.DateTime, default=datetime.utcnow)
    check_out_date = db.Column(db.DateTime, nullable=True)

    # Relationship to link maintenance requests with tenants
    maintenance_requests = db.relationship('MaintenanceRequest', back_populates='tenant', cascade="all, delete-orphan")

class MaintenanceRequest(db.Model):
    __tablename__ = 'maintenance_requests'
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)
    apartment_number = db.Column(db.String(10), nullable=False)
    problem_area = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    photo = db.Column(db.String(100), nullable=True)  # Path to uploaded photo
    status = db.Column(db.String(20), default='pending')

    # Link back to the tenant model
    tenant = db.relationship('Tenant', back_populates='maintenance_requests')
