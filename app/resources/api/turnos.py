from app.models.turno import Turno
from app.models.centro import Centro
from app.helpers.forms import TurnoForm
from flask import jsonify, request, abort, Response
from datetime import date, datetime, time, timedelta
import json


def turno_list(id, fecha=date.today()):
    """
    Devuelve un json que contiene el listado de los turnos disponibles para un centro de ayuda en un día en particular.
    En caso de no especificar una fecha, se devuelve la disponibilidad de turnos para el día consultado.

    """
    try:
        centro = Centro.with_id(id)
        if not centro:
            return Response('El centro no existe', status=400)
        turno = Turno.bloques_disponibles(id, str(fecha))
    except:
        return Response(status=500)
    data_turno = []

    for i in turno:
        date_time = datetime.strptime(i, "%H:%M") + timedelta(minutes=30)
        data_turno.append({
            "centro_id": id,
            "hora_inicio": i,
            "hora_fin": date_time.strftime("%H:%M"),
            "fecha": str(fecha)
        })

    final = json.dumps({"turnos": data_turno}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')


def turno_create(id):
    """
    Devuelve un json con la reserva de un turno para un centro de ayuda en particular,
    verificando que no se agreguen dos turnos para el mismo centro y con el mismo bloque de horario
    en un mismo día

    """
    data = request.get_json()
    form = TurnoForm(csrf_enabled=False)
    form.email = data['email']
    form.telefono = data['telefono']
    form.hora_inicio = data['hora_inicio']
    form.fecha = data['fecha']
    form.centro_id = data['centro_id']

    horaActual = datetime.now()
    horaActual = horaActual.strftime("%H:%M")
    if not form.validate_on_submit():
        return Response('Error de validacion', status=400)
    if not form.centro_id == id:
        return Response('Error de validacion del centro', status=400)

    date_time = datetime.strptime(data['hora_inicio'],
                                  "%H:%M") + timedelta(minutes=30)
    date_time = date_time.strftime("%H:%M")

    if form.fecha < str(datetime.today() + timedelta(days=-1)):
        return Response('La fecha debe ser mayor o igual a la fecha actual',
                        status=400)

    if (data['hora_fin'] > date_time) or (data['hora_fin'] < date_time):
        return Response('La hora fin de turno no coincide con lo esperado',
                        status=400)

    if form.fecha == str(date.today()):
        if (form.hora_inicio < horaActual):
            return Response(
                'La hora del turno debe ser mayor a la hora actual',
                status=400)
    try:

        centro = Centro.with_id(id)
        if not centro:
            return Response('El centro no existe', status=400)
        turnos_disponibles = Turno.bloques_disponibles(form.centro_id,
                                                       form.fecha)
        if form.hora_inicio not in turnos_disponibles:
            return Response('El turno no esta disponible', status=400)
        turno = Turno.add_and_return(data)

    except:
        return Response(status=400)



        return Response(status=400)
    turno_creado = {}

    turno_creado = {
        "centro_id": turno.centro_id,
        "email": turno.email,
        "telefono": turno.telefono,
        "hora_inicio": turno.hora_inicio.strftime("%H:%M"),
        "hora_fin": turno.hora_fin.strftime("%H:%M"),
        "fecha": str(turno.fecha)
    }

    final = json.dumps({"atributos": turno_creado}, indent=2)
    return Response(final, status=201)
