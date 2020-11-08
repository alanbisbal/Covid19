from flask import redirect, render_template, request, url_for, session, abort, flash,jsonify
from app import db
from app.models.config import Config
from app.helpers.auth import authenticated
from app.models.centro import Centro
from app.models.tipo_centro import Tipo_centro
from app.models.estado import Estado
from app.helpers.forms import CenterForm

from app.helpers import maps

from app.helpers.validates import form_config_update
from app.helpers.permits import has_permit, is_admin
import requests


def index():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_index'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # retorna todos los usuarios
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    centros = Centro.query.paginate(page,per_page,error_out=False)
    return render_template("centro/index.html", centros=centros)

def new():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    form = CenterForm()
    #tipos = Tipo_centro.all()
    estados = Estado.all()
    #form.tipo_centro.choices = [(t.id, t.nombre) for t in tipos]
    form.estado_id.choices = [(e.id, e.nombre) for e in estados]
    map = maps.index()
    return render_template("centro/new.html",form=form,map=map)

def create():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # validaciones de acceso administrador
    form = CenterForm()
    print("formulario", form)
    print("QUE ES PROTOCOLO?", form.protocolo)
    print("QUE TIENE FORM.DATA: ", form.data)
    #centro = Centro.with_id(data['centro_id']) #Seguir pensandolo
    Centro.add(form.data)
    flash("Insercion exitosa","success")
    return redirect(url_for("centro_index"))

def update(centro_id):
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_update'):
        flash("No posee permisos.","danger")
        return redirect(url_for("home"))
    tipos = Tipo_centro.all()
    centro = Centro.with_id(centro_id)
    form = CenterForm()
    tipos = Tipo_centro.all()
    estados = Estado.all()
    form.tipo_centro.choices = [(t.id, t.nombre) for t in tipos]
    form.tipo_centro.default = centro.tipo_centro # deberia ser algo de este estilo
    form.estado_id.choices = [(e.id, e.nombre) for e in estados]
    map = maps.showLoc(centro.latitud,centro.longitud)
    return render_template("centro/update.html",centro = centro, form=form,map=map)

def update_new():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_update'):
        flash("No posee permisos.","danger")
        return redirect(url_for("home"))

    Centro.add(form.data)
    flash("Actualización exitosa.","success")
    return redirect(url_for("centro_index"))

def delete():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_destroy'):
        flash("No posee permisos.","danger")
        return redirect(url_for("home"))

    centro = Centro.with_id(request.form['centro_id'])
    centro.delete()
    flash("Eliminación exitosa.","success")
    return redirect(url_for("centro_index"))

def search():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_index'):
        flash("No posee permisos.","danger")
        return redirect(url_for("home"))

    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    centros = Centro.query.paginate(page,per_page,error_out=False)
    estado = request.args.get("estado")
    filter = request.args.get("filtro")
    # se aplica filtro independientemente del estado
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    if estado == '---':
        centros = Centro.with_filter(filter).paginate(page,per_page,error_out=False)
        return render_template("centro/index.html", centros=centros, estado=estado)
    # se aplica filtro con estado activo
    if estado == 'publicado':
        centros = Centro.publicate(filter).paginate(page,per_page,error_out=False)
        return render_template("centro/index.html", centros=centros, estado=estado)
    if estado == 'despublicado':
        centros = Centro.despublicate(filter).paginate(page,per_page,error_out=False)
        return render_template("centro/index.html", centros=centros, estado=estado)
    # se aplica filtro con estado inactivo
    centros = Centro.pending(filter).paginate(page,per_page,error_out=False)
    return render_template("centro/index.html", centros=centros, estado=estado)


    return redirect(url_for("centro_index"))

def show(centro_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_show'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # validacion de acceso administrador y si lo es retorna el usuario enviado por id
    centro = Centro.with_id(centro_id)
    map = maps.showLoc(centro.latitud,centro.longitud)
    return render_template("centro/show.html",centro = centro,map=map)
