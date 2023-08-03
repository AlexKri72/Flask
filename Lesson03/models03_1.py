from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80),  nullable=False)
    age = db.Column(db.Integer,  nullable=False)
    gender = db.Column(db.String(5),  nullable=False)
    group = db.Column(db.String(20),  nullable=False)
    id_facultet = db.Column(db.Integer, db.ForeignKey('facultet.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Student{self.name} {self.lastname} {self.age} {self.gender} {self.created_at}'

class Facultet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fac_name = db.Column(db.String(80), nullable=False)
    student = db.relationship('student', backref='facultet')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'Facultet{self.fac_name}'
