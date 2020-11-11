from app.models.turno import Turno
from flask import jsonify, request, abort
from datetime import date


def turno_list(id,fecha=date.today()):
    try:
     turno= Turno.with_id_fecha(id,fecha)    
    except:
        abort(500)

    data_turno = []

    for i in turno:
        data_turno.append({
            "centro_id": str(i.centro_id),
            "email": i.email,
            "hora_inicio": str(i.hora_inicio),
            "hora_fin": str(i.hora_fin),
            "fecha": str(i.fecha)
        })

    return jsonify(turnos=data_turno)
