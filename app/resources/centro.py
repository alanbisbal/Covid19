from flask import redirect, render_template, request, url_for, session, abort, flash,jsonify
from app import db
from app.models.config import Config
from app.helpers.auth import authenticated
from app.models.centro import Centro
from app.helpers.forms import CenterForm

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

    municipios = requests.get("https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios").json()
    form = CenterForm()
    return render_template("centro/new.html",form=form)

def create():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_new'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # validaciones de acceso administrador
    data = request.form
    municipios = requests.get("https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios").json()['data']['Town']
    for mun in municipios:
        if municipios[mun]['name'] == data['municipio_id']:
            id=municipios[mun]['id']
    Centro.add(data,id)
    flash("Insercion exitosa","success")
    return redirect(url_for("centro_index"))

def update(centro_id):
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_update'):
        flash("No posee permisos.","danger")
        return redirect(url_for("home"))
    centro = Centro.with_id(centro_id)
    form = CenterForm()
    return render_template("centro/update.html",centro = centro, form=form)

def update_new():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_update'):
        flash("No posee permisos.","danger")
        return redirect(url_for("home"))
    data= request.form
    # Hacer todas estas funciones para el centro
    centro = Centro.with_id(data['centro_id']) #Seguir pensandolo
    municipios = requests.get("https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios").json()['data']['Town']
    for mun in municipios:
        if municipios[mun]['name'] == data['municipio_id']:
            id=municipios[mun]['id']

    centro.update(data, id)
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
    return redirect(url_for("centro_index"))

def show(centro_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_show'):
        flash("No posee permisos","danger")
        return redirect(url_for("home"))
    # validacion de acceso administrador y si lo es retorna el usuario enviado por id
    centro = Centro.with_id(centro_id)
    return render_template("centro/show.html",centro = centro)
