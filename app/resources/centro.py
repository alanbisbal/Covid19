from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from app import db
from app.models.config import Config
from app.helpers.auth import authenticated
from app.models.centro import Centro
from app.models.tipo_centro import Tipo_centro
from app.models.estado import Estado
from app.helpers.forms import CenterForm

from app.helpers.validates import form_config_update, sanitizar_input
from app.helpers.permits import has_permit, is_admin
import requests
import bleach


def index():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así muestra el listado de centros paginados de acuerdo a los elementos almacenados en la configuración

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('centro_index'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    centros = Centro.query.paginate(page, per_page, error_out=False)

    return render_template("centro/index.html", centros=centros)


def new():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así muestra el formulario para la creacion de un centro habiendo cargado previamente al formulario
    con todos los tipos de centro y estado

    """
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
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así carga el formulario con los datos ingresados y crea el centro

    """
    if not authenticated(session):
        abort(401)
    if not has_permit('centro_new'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    form = CenterForm()
    if not form.validate_on_submit():
        return redirect(request.referrer)
    sanitizar_input(form)
    Centro.add(form.data)
    flash("Insercion exitosa", "success")

    return redirect(url_for("centro_index"))


def update(centro_id):
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así a partir de un centro en particular muestra la información previamente cargada en
    la creación del mismo

    """
    if not authenticated(session):
        abort(401)

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
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así obtiene los nuevos datos cargados en el formulario y realiza la actualización del mismo
    realizando previamente las validaciones correspondientes a los datos ingresados.
    """
    if not authenticated(session):
        abort(401)

    if not has_permit('centro_update'):
        flash("No posee permisos.", "danger")
        return redirect(url_for("home"))

    sanitizar_input(form)
    form = CenterForm()
    centro = Centro.with_id(request.form['centro_id'])

    if not form.validate_on_submit() or not centro:
        return redirect(request.referrer)

    centro.update(form.data)
    flash("Actualización exitosa.", "success")

    return redirect(url_for("centro_index"))


def delete():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así elimina el centro seleccionado siempre y cuando este no esté asignado a un turno

    """
    if not authenticated(session):
        abort(401)

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
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así pagina el listado de centros de acuerdo a los elementos almacenados en la configuración,
    mostrando los centros de ayuda que coincidan con la opción de búsqueda ingresada y/o seleccionada

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('centro_index'):
        flash("No posee permisos.", "danger")
        return redirect(url_for("home"))

    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    centros = Centro.query.paginate(page, per_page, error_out=False)
    estado = request.args.get("estado")
    filter = request.args.get("filtro")

    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)

    if estado == '---':
        centros = Centro.with_filter(filter).paginate(page,
                                                      per_page,
                                                      error_out=False)
        return render_template("centro/index.html",
                               centros=centros,
                               estado=estado)

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

    centros = Centro.pendiente(filter).paginate(page,
                                                per_page,
                                                error_out=False)
    return render_template("centro/index.html", centros=centros, estado=estado)

    return redirect(url_for("centro_index"))


def show(centro_id):
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así a partir de un centro en particular muestra los datos del mismo.

    """
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
    """
     Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
     de ser así muestra el listado de centros pendientes paginados de acuerdo a los elementos almacenados
     en la configuración .

    """
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
    """
     Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
     de ser así a partir de un centro en particular,pública dicho centro .

    """
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
    """
     Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
     de ser así a partir de un centro en particular,despublica dicho centro .

    """
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
