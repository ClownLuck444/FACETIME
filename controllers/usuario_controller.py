from flask import Blueprint, request,jsonify
import numpy as np
import face_recognition
from models import db
from models import usuario,asistencia
from datetime import datetime,timedelta,timezone
usuario_bp=Blueprint('usuario_bp', __name__)

@usuario_bp.route('/validacion', methods=['POST'])
def entrada():
    data=request.get_json()
    face_descriptor=np.array(data['face_descriptor'])

    known_face=[]
    know_ids=[]

    usuarios=usuario.query.all()
    for usuario in usuarios:
        known_face_descriptor=np.array(usuario.face_descriptor)
        known_face.append=np.array(usuario.face_descriptor)
        know_ids.append(usuario.idUsuario)

    results = face_recognition.compare_faces(known_face, face_descriptor)
    face_distances = face_recognition.face_distance(known_face, face_descriptor)
    best_match_index = np.argmin(face_distances)

    if results[best_match_index]:
        idUsuario = know_ids[best_match_index]
        # Register check-in for the employee
        now = datetime.now(timezone.utc)
        attendance = asistencia(idUsuario=idUsuario, check_in=now, date=now.date())
        db.session.add(attendance)
        db.session.commit()
        return jsonify({"message": "SU MARCACION SE REGISTRO CON ÉXITO"}), 200
    else:
        return jsonify({"message": "Usted es un impostor"}), 400