from app.models.centro import Centro
from app.models.tipo_centro import Tipo_centro
from app.models.estado import Estado
from app.models.config import Config
from app.helpers.forms import CenterForm
from app.db import db
from flask import jsonify, request, abort, Response
import base64
import json
import io

def center_list():
    per_page = Config.getConfig().elementos

    try:
        page = int(request.args["page"])
    except:
        page = 1

    try:
        centros_paginados = Centro.query.filter_by(estado_id=1).paginate(page,per_page,error_out=False)
    except:
        return Response(status=500)

    data_centro = []

    total= Centro.count_approved()

    for i in centros_paginados.items:
        data_centro.append({
            "nombre": i.nombre,
            "direccion": i.direccion,
            "telefono": i.telefono,
            "hora_inicio": str(i.hora_inicio),
            "hora_fin": str(i.hora_fin),
            "web": i.web,
            "email": i.email,
            "tipo": str(Tipo_centro.with_id(i.tipo_centro).nombre)
        })

    final = json.dumps({"centros": data_centro, "total": total, "pagina": page}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')


def center(id):

    try:
        centro= Centro.with_id(id)
    except:
        return Response(status=500)

    centro_data={}

    if not centro:
        return Response(status=401)
    else:
        centro_data={
            "nombre": centro.nombre,
            "direccion": centro.direccion,
            "telefono": centro.telefono,
            "hora_inicio": str(centro.hora_inicio),
            "hora_fin": str(centro.hora_fin),
            "web": centro.web,
            "email": centro.email,
            "tipo": Tipo_centro.with_id(centro.tipo_centro).nombre
        }

    final = json.dumps({"atributos": centro_data}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')


def center_create():
    try:
        form= CenterForm(csrf_enabled=False)
        form.nombre= request.form['nombre']
        form.direccion= request.form['direccion']
        form.telefono= request.form['telefono']
        form.hora_inicio= request.form['hora_inicio']
        form.hora_fin= request.form['hora_fin']
        form.municipio_id= request.form['municipio_id']
        #form.protocolo = request.form['protocolo']
        form.web= request.form['web']
        form.email= request.form['email']
        form.estado_id= request.form['estado_id']
        form.latitud= request.form['latitud']
        form.longitud= request.form['longitud']
        form.tipo_centro= request.form['tipo_centro']
        if not form.validate_on_submit():
            return Response(status=400)
        centro = Centro.add(form.data)
    except:
        return Response(status=500)
    if not centro:
        return Response(status=400)

    centro_creado= {}

    centro_creado={
        "nombre": centro.nombre,
        "direccion": centro.direccion,
        "telefono": centro.telefono,
        "hora_inicio": str(centro.hora_inicio),
        "hora_fin": str(centro.hora_fin),
        "web": centro.web,
        "email": centro.email,
        "tipo": Tipo_centro.with_id(centro.tipo_centro).nombre
    }

    final = json.dumps({"atributos": centro_creado}, indent=2)
    return Response(final, status=201)
