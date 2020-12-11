from app.models.centro import Centro
from app.models.tipo_centro import Tipo_centro
from app.models.estado import Estado
from app.models.config import Config
from app.helpers.forms import CenterForm
from app.helpers.validates import validar_municipio, sanitizar_input
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
        centros_paginados = Centro.query.filter_by(estado_id=1).paginate(
            page, per_page, error_out=False)
        centros_paginados = Centro.publicados().paginate(page,
                                                         per_page,
                                                         error_out=False)

    except:
        return Response(status=500)

    data_centro = []

    total = Centro.count_approved()

    for i in centros_paginados.items:
        data_centro.append({
            "id":
            i.id,
            "nombre":
            i.nombre,
            "direccion":
            i.direccion,
            "telefono":
            i.telefono,
            "hora_inicio":
            str(i.hora_inicio),
            "hora_fin":
            str(i.hora_fin),
            "web":
            i.web,
            "email":
            i.email,
            "latitud":
            i.latitud,
            "longitud":
            i.longitud,
            "tipo":
            str(Tipo_centro.with_id(i.tipo_centro).nombre)
        })

    final = json.dumps({
        "centros": data_centro,
        "total": total,
        "pagina": page
    },
                       indent=2,
                       ensure_ascii=False)
    return Response(final, mimetype='application/json')


def center(id):

    try:
        centro = Centro.with_id(id)
    except:
        return Response(status=500)

    centro_data = {}

    if not centro:
        return Response(status=401)
    else:
        centro_data = {
            "id": centro.id,
            "nombre": centro.nombre,
            "direccion": centro.direccion,
            "telefono": centro.telefono,
            "hora_inicio": str(centro.hora_inicio),
            "hora_fin": str(centro.hora_fin),
            "web": centro.web,
            "email": centro.email,
            "tipo": Tipo_centro.with_id(centro.tipo_centro).nombre
        }

    final = json.dumps({"atributos": centro_data},
                       indent=2,
                       ensure_ascii=False)
    return Response(final, mimetype='application/json')


def center_create():
    try:
        data = request.get_json()

        data['hora_inicio'] = data['hora_apertura']
        data['hora_fin'] = data['hora_cierre']
        tipo = Tipo_centro.with_name(data['tipo'])
        data['estado_id'] = 3
        data['tipo_centro'] = tipo.id
        data['municipio_id'] = ''

        form = CenterForm(csrf_enabled=False)
        form.nombre = data['nombre']
        form.direccion = data['direccion']
        form.telefono = data['telefono']
        form.hora_inicio = data['hora_inicio']
        form.hora_fin = data['hora_fin']
        form.web = data['web']
        form.email = data['email']
        form.tipo_centro = data['tipo_centro']
        form.estado_id = data['estado_id']
        form.latitud = data['latitud']
        form.longitud = data['longitud']
        form.municipio_id = data['municipio_id']

        tieneArroba = False
        if not form.validate_on_submit():
            return Response('Error de datos de formulario', status=400)
        if form.email != "":
            for char in form.email:
                if char == "@":
                    tieneArroba = True
                    break
        if form.email != "" and tieneArroba == False:
            return Response('Error de datos de formulario', status=400)

        sanitizar_input(form)
        centro = Centro.add(form.data)
        if not centro:
            return Response('El centro no existe', status=400)
    except:
        return Response('Error de servidor', status=500)

    centro_creado = {}

    centro_creado = {
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


def center_types():
    data = []
    tipos = Tipo_centro.all()
    for i in tipos:
        data.append({"id": i.id, "nombre": i.nombre})

    final = json.dumps({"tipos": data}, indent=2, ensure_ascii=False)
    return Response(final, mimetype='application/json')
