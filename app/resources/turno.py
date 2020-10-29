from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection

from app.models.turno import Turno
from app.models.centro import Centro
from app.models.config import Config

from app.helpers.auth import authenticated

#from app.helpers.validates import
from app.helpers.permits import has_permit, is_admin


def index(centro):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_index'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # retorna todos los turnos
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    turnos = Turno.with_filter(centro).paginate(page,per_page,error_out=False)
    return render_template("turno/index.html", turnos=turnos)

def new():
    turnos = Turno.all()
    # retorna vista de creacion de usuario
    return render_template("turno/new.html",turnos=turnos)

def create():
    data = request.form
    if not form_turno(data):
        return redirect(request.referrer)
    
    flash("Insercion exitosa","success")
    return redirect(url_for("turno_index"))    

def update(turno_id):
    turno = Turno.with_id(turno_id)
    return render_template("turno/update.html",turno = turno)

def update_new():
    data = request.form
    if not form_turno(data):
        return redirect(request.referrer)
    turno.update(data)
    flash("Actualización exitosa.","success")
    return redirect(url_for('turno_index'))  

def delete():
    # se busca el usuario en la base de datos y se lo elimina
    turno = Turno.with_id(request.form['turno_id'])
    turno.delete()
    flash("Eliminación exitosa.","success")
    return redirect(url_for('turno_index'))  