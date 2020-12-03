from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from app import db
from app.models.config import Config
from app.helpers.auth import authenticated
from app.models.centro import Centro
from app.models.tipo_centro import Tipo_centro
from app.models.estado import Estado
from app.helpers.forms import CenterForm

from app.helpers.validates import form_config_update
from app.helpers.permits import has_permit, is_admin
import requests


def index():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_index'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    # retorna todos los usuarios
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    centros = Centro.query.paginate(page, per_page, error_out=False)
    return render_template("centro/index.html", centros=centros)


def new():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_new'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    form = CenterForm()
    tipos = Tipo_centro.all()
    estados = Estado.all()
    form.tipo_centro.choices = [(t.id, t.nombre) for t in tipos]
    form.estado_id.choices = [(e.id, e.nombre) for e in estados]

    return render_template("centro/new.html", form=form)


def create():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_new'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    # validaciones de acceso administrador
    form = CenterForm()
    if not form.validate_on_submit():
        return redirect(request.referrer)
    #centro = Centro.with_id(data['centro_id']) #Seguir pensandolo
    Centro.add(form.data)
    flash("Insercion exitosa", "success")
    return redirect(url_for("centro_index"))


def update(centro_id):
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_update'):
        flash("No posee permisos.", "danger")
        return redirect(url_for("home"))
    centro = Centro.with_id(centro_id)
    if not centro:
        flash("Url invalida.", "danger")
        return redirect(url_for("home"))
    form = CenterForm()
    form.municipio_id.default = centro.municipio_id
    form.tipo_centro.default = centro.tipo.id
    form.estado_id.default = centro.estado_id
    form.protocolo.value = centro.protocolo
    form.hora_inicio.default = centro.hora_inicio
    form.hora_fin.default = centro.hora_fin
    form.process()
    return render_template("centro/update.html", centro=centro, form=form)


def update_new():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_update'):
        flash("No posee permisos.", "danger")
        return redirect(url_for("home"))
    form = CenterForm()
    centro = Centro.with_id(request.form['centro_id'])
    if not form.validate_on_submit() or not centro:
        return redirect(request.referrer)
    centro.update(form.data)
    flash("Actualización exitosa.", "success")
    return redirect(url_for("centro_index"))


def delete():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_destroy'):
        flash("No posee permisos.", "danger")
        return redirect(url_for("home"))

    centro = Centro.with_id(request.form['centro_id'])
    if not centro:
        flash("Url invalida.", "danger")
        return redirect(url_for("home"))
    if centro.turnos:
        flash("No se puede eliminar ya que el centro posee turnos.", "danger")
        return redirect(url_for("centro_index"))
    centro.delete()
    flash("Eliminación exitosa.", "success")
    return redirect(url_for("centro_index"))


def search():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    if not has_permit('centro_index'):
        flash("No posee permisos.", "danger")
        return redirect(url_for("home"))

    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    centros = Centro.query.paginate(page, per_page, error_out=False)
    estado = request.args.get("estado")
    filter = request.args.get("filtro")
    # se aplica filtro independientemente del estado
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    if estado == '---':
        centros = Centro.with_filter(filter).paginate(page,
                                                      per_page,
                                                      error_out=False)
        return render_template("centro/index.html",
                               centros=centros,
                               estado=estado)
    # se aplica filtro con estado activo
    if estado == 'publicado':
        centros = Centro.publicate(filter).paginate(page,
                                                    per_page,
                                                    error_out=False)
        return render_template("centro/index.html",
                               centros=centros,
                               estado=estado)
    if estado == 'despublicado':
        centros = Centro.despublicate(filter).paginate(page,
                                                       per_page,
                                                       error_out=False)
        return render_template("centro/index.html",
                               centros=centros,
                               estado=estado)
    # se aplica filtro con estado inactivo
    centros = Centro.pendiente(filter).paginate(page,
                                                per_page,
                                                error_out=False)
    return render_template("centro/index.html", centros=centros, estado=estado)

    return redirect(url_for("centro_index"))


def show(centro_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_show'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    # validacion de acceso administrador y si lo es retorna el usuario enviado por id
    centro = Centro.with_id(centro_id)
    if not centro:
        flash("Url invalida.", "danger")
        return redirect(url_for("home"))
    return render_template("centro/show.html", centro=centro)


def pendientes():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_show'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    centros = Centro.pending().paginate(page, per_page, error_out=False)
    return render_template("centro/pendientes.html", centros=centros)


def publicar():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_show'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    centro = Centro.with_id(request.args.get("centro_id"))
    if not centro:
        flash("Url invalida.", "danger")
        return redirect(url_for("home"))
    centro.publicar()
    return redirect(request.referrer)


def despublicar():
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_show'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    centro = Centro.with_id(request.args.get("centro_id"))
    if not centro:
        flash("Url invalida.", "danger")
        return redirect(url_for("home"))
    centro.despublicar()
    return redirect(request.referrer)
