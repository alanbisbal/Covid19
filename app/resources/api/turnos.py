from app.models.turno import Turno
from app.models.centro import Centro
from app.helpers.forms import TurnoForm
from flask import jsonify, request, abort,Response
from datetime import date
import json


def turno_list(id,fecha=date.today()):
    try:
     turno= Turno.with_id_fecha(id,fecha)
    except:
        return Response(status=500)

    data_turno = []

    for i in turno:
        data_turno.append({
            "centro_id": str(i.centro_id),
            "email": i.email,
            "hora_inicio": str(i.hora_inicio),
            "hora_fin": str(i.hora_fin),
            "fecha": str(i.fecha)
        })

    final = json.dumps({"turnos": data_turno}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')


def turno_create(id):
    form= TurnoForm(csrf_enabled=False)
    form.email= request.form['email']
    form.telefono= request.form['telefono']
    form.hora_inicio= request.form['hora_inicio']
    form.fecha= request.form['fecha']
    form.centro_id= id
    if not form.validate_on_submit():
        print("errores de validacion",form.errors)
        return Response("soyElerror",status=400)

    try:
        centro = Centro.with_id(id)
        print("centro",Centro.with_id(id))
        if not centro:
            return Response(status=400)
        turnos_disponibles=Turno.bloques_disponibles(form.centro_id,form.fecha)
        if id == form.centro_id:
            if str(form.hora_inicio) not in  turnos_disponibles:
                return Response('el turno no esta disponible',status=400)
        turno = Turno.add_and_return(form.data)

    except:
        return Response(status=400)



    turno_creado= {}

    turno_creado={
        "centro_id": turno.centro_id,
        "email": turno.email,
        "telefono":turno.telefono,
        "hora_inicio": str(turno.hora_inicio),
        "hora_fin": str(turno.hora_fin),
        "fecha": str(turno.fecha)
     }

    final = json.dumps({"atributos": turno_creado}, indent=2)
    return Response(final, status=201)
