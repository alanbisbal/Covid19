from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection

from app.models.turno import Turno
from app.models.centro import Centro
from app.models.config import Config

from app.helpers.auth import authenticated

from app.helpers.forms import TurnoForm

#from app.helpers.validates import
from app.helpers.permits import has_permit, is_admin


def index(centro_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_index'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # retorna todos los turnos
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    print (centro_id)
    turnos = Turno.with_filter(centro_id).paginate(page,per_page,error_out=False)
    return render_template("turno/index.html", turnos=turnos)

def new():
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    form = TurnoForm()
    # retorna vista de creacion de turnos
    return render_template("turno/new.html",form=form)

def create():
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    data = request.form
    Turno.add(data)
    flash("Insercion exitosa","success")
    return redirect(url_for("turno_index"))

def update(turno_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_update'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    turno = Turno.with_id(turno_id)
    return render_template("turno/update.html",turno = turno)

def update_new():
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_update'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    data = request.form
    if not form_turno(data):
        return redirect(request.referrer)
    turno.update(data)
    flash("Actualización exitosa.","success")
    return redirect(url_for('turno_index'))

def delete():
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_destroy'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # se busca el usuario en la base de datos y se lo elimina
    turno = Turno.with_id(request.form['turno_id'])
    turno.delete()
    flash("Eliminación exitosa.","success")
    return redirect(url_for('turno_index'))
