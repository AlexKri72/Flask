# ������� ���� ������ ��� �������� ���������� � ������ � ����������.
# ���� ������ ������ ��������� ��� �������: "�����" � "������".
# � ������� "�����" ������ ���� ��������� ����: id, ��������, ��� �������, ���������� ����������� � id ������.
# � ������� "������" ������ ���� ��������� ����: id, ��� � �������.
# ���������� ������� ����� ����� ��������� "�����" � "������".
# �������� �������-����������, ������� ����� �������� ������ ���� ���� � ��������� �� �������.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer,  nullable=False)
    quantity = db.Column(db.Integer,  nullable=False)
    id_autor = db.Column(db.Integer, db.ForeignKey('Autors.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Book{self.title} {self.year} {self.quantity} {self.created_at}'

class Autors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    books = db.relationship('books', backref='autors',lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Autor {self.name}{self.last_name}'
