from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection

from app.models.turno import Turno
from app.models.centro import Centro
from app.models.config import Config

from app.helpers.auth import authenticated

from app.helpers.forms import TurnoForm, NewTurnoForm, SearchForm

#from app.helpers.validates import
from app.helpers.permits import has_permit, is_admin
from datetime import datetime,time,timedelta,date


def index(centro_id = None):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_index'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # retorna todos los turnos
    form =  NewTurnoForm()
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    if centro_id:
        turnos = Turno.with_next_two_date(centro_id).paginate(page,per_page,error_out=False)
        form.fecha.data = date.today()
        return render_template("turno/index.html", turnos=turnos, centro_id=centro_id, form=form)
    else:
        search = SearchForm()
        centros = Centro.all()
        form.centro_id.choices = [(e.id, e.nombre) for e in centros]
        search.centro.choices = [(e.nombre) for e in centros]
        form.fecha.data = date.today()
        turnos = Turno.with_next_two().paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos, form=form, buscador=search)


def new(centro_id = None):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    data = request.args
    form = TurnoForm()
    fecha = datetime.strptime(data["fecha"], '%Y-%m-%d')
    form.fecha.data = fecha
    if(fecha.today() < datetime.today()):
        flash("la fecha no puede ser menor a la fecha actual","danger")
        return redirect(url_for("home"))
    if centro_id:
        form.centro_id.data = centro_id
    else:
        form.centro_id.data = data["centro_id"]
    form.hora_inicio.choices = Turno.bloques_disponibles(form.centro_id.data,request.args['fecha'])
    return render_template("turno/new.html",form=form)

def create():
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    form = TurnoForm()
    if not form.validate_on_submit():
        print('errores',form.errors)
        flash("El tipo de dato ingresado es incorrecto","danger")
        return redirect(request.referrer)
    hora = datetime.strptime(form.data['hora_inicio'], '%H:%M:%S')
    if not (hora.minute == 00 or hora.minute == 30):
        flash("El horario debe finalizar con los minutos xx:00 o xx:30","danger")
        return redirect(url_for('turno_index', centro_id=form.centro_id.data))
    turnos_disponibles=Turno.bloques_disponibles(form.data['centro_id'],str(form.data['fecha']))
    if str(form.data['hora_inicio']) not in  turnos_disponibles:
        flash("Bloque de turno ocupado","danger")
        return redirect(url_for('turno_index', centro_id=form.centro_id.data))
    Turno.add(form.data)
    flash("Insercion exitosa","success")
    return redirect(url_for('turno_index', centro_id=form.centro_id.data))

def update(turno_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_update'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    turno = Turno.with_id(turno_id)
    form = TurnoForm()
    form.fecha.data = turno.fecha
    form.hora_inicio.choices = Turno.bloques_disponibles(turno.centro_id,str(form.fecha.data))

    return render_template("turno/update.html",form = form,turno=turno)

def update_new():
    if not authenticated(session):
        abort(401)
    if not has_permit('turno_update'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    form = TurnoForm()
    turno = Turno.with_id(request.form['turno_id'])
    if not form.validate_on_submit() or not turno:
        print(form.errors)
        flash("El tipo de dato ingresado es incorrecto","danger")
        return redirect(request.referrer)
    hora = datetime.strptime(form.data['hora_inicio'], '%H:%M:%S')
    if not (hora.minute == 00 or hora.minute == 30):
        flash("El horario debe finalizar con los minutos xx:00 o xx:30","danger")
        return redirect(url_for('turno_index', centro_id=form.centro_id.data))
    turnos_disponibles=Turno.bloques_disponibles(form.data['centro_id'],str(form.data['fecha']))
    if str(form.data['hora_inicio']) not in  turnos_disponibles:
        flash("Bloque de turno ocupado","danger")
    turno.update(form.data)
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
    centros = Centro.all()
    form =  NewTurnoForm()
    form.centro_id.choices = [(e.id, e.nombre) for e in centros]
    if centro_id:
        centro = Centro.with_id(centro_id)
        turnos = Turno.with_email_centro(email,centro.nombre).paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos,centro_id=centro_id,form = form)
    centro = request.args.get("centro")
    search = SearchForm()
    search.centro.choices = [(e.nombre) for e in centros]
    # para el buscador de  turnos de todos los centros
    data = request.args
    if data['centro']=="" and data['email'] == "":
        turnos = Turno.query.paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos,form = form, buscador=search)
    if data['centro'] != "" and data['email'] == "":
        turnos = Turno.with_nombre_centro(data['centro']).paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos,form = form, buscador=search)
    if data['centro'] == "" and data['email'] != "":
        turnos = Turno.with_email(data['email']).paginate(page,per_page,error_out=False)
        return render_template("turno/index.html", turnos=turnos,form = form)
    turnos = Turno.with_email_centro(data['email'],data['centro']).paginate(page,per_page,error_out=False)
    return render_template("turno/index.html", turnos=turnos,form = form, buscador=search)
