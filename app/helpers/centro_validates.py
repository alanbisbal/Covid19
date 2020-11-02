from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.centro import Centro

def form_centro_update(data):
    ok = True
    if not data['name']:
        flash('El nombre del centro no puede estar vacio',"danger")
        ok = False
    if not data['address']:
        flash('La direccion del centro no puede estar vacia',"danger")
        ok = False
    if not data['phone']:
        flash('El telefono no puede estar vacio',"danger")
        ok = False
    if not data['open']:
        flash('El horario de apertura no puede estar vacio',"danger")
        ok = False
    if not data['close']:
        flash('El horario de cierre no puede estar vacio',"danger")
        ok = False
    if not data['municipio_id']:
        flash('El id del municipio no puede estar vacio',"danger")
        ok = False
    if not data['web']:
        #Puede no tener web
        ok = True
    if not data['email']:
        #Puede no tener email
        ok = True
    if not data['state']:
        flash('El estado no puede estar vacio',"danger")
        ok = False
    if not data['protocol']:
        flash('El protocolo no puede estar vacio',"danger")
        ok = False
    if not data['coordinates']:
        flash('Las coordenadas no pueden estar vacias',"danger")
        ok = False
    if not data['type']:
        flash('El tipo no puede estar vacio',"danger")
        ok = False
    if not data['turnos']:
        flash('Los turnos no pueden estar vacios',"danger")
        ok = False
    if ok:
        return True
    else:
        return False

def exist_centro_email_update(data,email):
    if data != email:
        centro = Centro.with_email(data)
        if centro:
            flash("El email ya existe en el sistema.","danger")
            return True
        else:
            return False
    return False
