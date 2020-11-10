from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection

from app.models.turno import Turno
from app.models.centro import Centro
from app.models.config import Config

from app.helpers.auth import authenticated

from app.helpers.forms import TurnoForm, TurnoFormAll

#from app.helpers.validates import
from app.helpers.permits import has_permit, is_admin


def index(centro_id = None):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_index'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # retorna todos los turnos
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    if centro_id:
        turnos = Turno.with_centro_id(centro_id).paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos, centro_id=centro_id)
    else:
        turnos = Turno.query.paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos)


def new(centro_id = None):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    if centro_id:
        form = TurnoForm()
        return render_template("turno/new.html",form=form, centro_id=centro_id)
    else:
        form = TurnoFormAll()
        centros = Centro.all()
        form.centro_id.choices = [(t.id, t.nombre) for t in centros]
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
    return redirect(url_for('turno_index', centro_id=data['centro_id']))

def update(turno_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_update'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    turno = Turno.with_id(turno_id)
    form = TurnoForm()
    return render_template("turno/update.html",form = form,turno=turno)

def update_new():
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_update'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    data = request.form
    turno = Turno.with_id(data['turno_id'])
    turno.update(data)
    flash("Actualización exitosa.","success")
    return redirect(url_for('turno_index', centro_id=turno.centro_id))

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
    return redirect(url_for('turno_index', centro_id=turno.centro_id))

def show(turno_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_show'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # validacion de acceso administrador y si lo es retorna el usuario enviado por id
    turno = Turno.with_id(turno_id)
    return render_template("turno/show.html",turno = turno)

def search(centro_id = None):
    if not authenticated(session):
        abort(401)
    # validacion de acceso
    if not has_permit('turno_index'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))

    email = request.args.get("email")
    filter = request.args.get("filtro")
    # se aplica filtro independientemente del email
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    # para el buscador de  turnos de centro en particular
    if centro_id:
        turnos = Turno.with_email_centro_id(email,centro_id).paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos,centro_id=centro_id)
    centro = request.args.get("centro")
    # para el buscador de  turnos de todos los centros
    if centro=="" and email == "":
        turnos = Turno.query.paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos)
    if centro != "" and email == "":
        turnos = Turno.with_nombre_centro(centro).paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos)
    if centro == "" and email != "":
        turnos = Turno.with_email(email).paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos)
    turnos = Turno.with_email_centro(email,centro).paginate(page,per_page,error_out=False)
    return render_template("turno/index.html", turnos=turnos)
