from app.models.centro import Centro
from flask import jsonify, request, abort


def center_list():
    try:
        centro= Centro.all()
    except:
        abort(500)

    data_centro = []

    for i in centro:
        data_centro.append({
            "nombre": i.nombre,
            "direccion": i.direccion,
            "telefono": i.telefono,
            "hora_inicio": str(i.hora_inicio),
            "hora_fin": str(i.hora_fin),
            "tipo": i.tipo_centro,
            "web": i.web,
            "email": i.email

            #NOTA: Agregar el total de elementos que se muestran por pagina

            #total
            #pagina
        })

    return jsonify(centros=data_centro)


def center(id):
    try:
        centro= Centro.with_id(id)
    except:
        abort(500)

    centro_data={}

    if not centro:
        abort(404)
    else:
        centro_data={
            "nombre": centro.nombre,
            "direccion": centro.direccion,
            "telefono": centro.telefono,
            "hora_inicio": str(centro.hora_inicio),
            "hora_fin": str(centro.hora_fin),
            "tipo": centro.tipo_centro,
            "web": centro.web,
            "email": centro.email
        }

    return jsonify(centro=centro_data)
