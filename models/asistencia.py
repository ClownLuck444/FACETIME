from . import db
from datetime import datetime

class Asistencia(db.Model):
    __tablename__="Asistencia"
    idAsistencia = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('Usuario.idUsuario'))
    entrada = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    salida = db.Column(db.DateTime)
    break_entrada = db.Column(db.DateTime)
    break_salida = db.Column(db.DateTime)
    tardanza = db.Column(db.Boolean, default=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())
