from . import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__="Usuario"
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    face_descriptor = db.Column(db.PickleType, nullable=False)
    idAsistencia=db.relationship('Asistencias',backref='usuario',lazy=True)


