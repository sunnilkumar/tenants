# tenant_management.models.py
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tenant(db.Model):
    tenant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    debt = db.Column(db.Float)
    rent = db.Column(db.Float)
    days_overdue = db.Column(db.Integer)
    status = db.Column(db.String)
    telephone = db.Column(db.String)
    email = db.Column(db.String)
    unit_number = db.Column(db.String)
    lease_start = db.Column(db.String)
    notes = db.Column(db.String)
    payment_status = db.Column(db.String, default="Paid")

class TenantUpdateHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.tenant_id'), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    changes = db.Column(db.Text, nullable=False)