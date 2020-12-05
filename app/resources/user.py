from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection

from app.models.user import User
from app.models.rol import Rol

from app.models.users_rols import Users_rols
from app.helpers.auth import authenticated

from app import db
from app.models.config import Config

from app.helpers.forms import ConfigForm

from app.helpers.validates import form_user_new, exist_email, exist_username, form_user_update, exist_email_update, exist_username_update, sanitizar_input
from app.helpers.permits import has_permit, is_admin
import bleach


def index():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así muestra el listado de usuarios paginados de acuerdo a los elementos almacenados en la configuración

    """
    if not authenticated(session):
        abort(401)
    if not has_permit('user_index'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    # retorna todos los usuarios
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    users = User.query.paginate(page, per_page, error_out=False)
    return render_template("user/index.html", users=users)


def new():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así muestra el formulario para la creacion de un usuario habiendo cargado previamente al formulario
    con todos los roles

    """
    if not authenticated(session):
        abort(401)
    if not has_permit('user_new'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))
    rols = Rol.all()
    # retorna vista de creacion de usuario
    return render_template("user/new.html", rols=rols)


def create():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así carga el formulario con los datos ingresados y crea al usuario

    """
    if not authenticated(session):
        abort(401)
    if not has_permit('user_new'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    data = request.form
    if not form_user_new(data):
        return redirect(request.referrer)

    if exist_email(data['email']):
        return redirect(request.referrer)

    if exist_username(data['username']):
        return redirect(request.referrer)

    if data['activo'] == 'True':
        estado = 1
    if data['activo'] == 'False':
        estado = 0

    dictUser = {}

    dictUser = {
        "username": bleach.clean(data['username']),
        "first_name": bleach.clean(data['first_name']),
        "last_name": bleach.clean(data['last_name']),
        "email": bleach.clean(data['email']),
        "password": bleach.clean(data['password'])
    }

    User.add(dictUser, estado)

    user = User.with_email(data['email'])
    roles = request.form.getlist('roles[]')
    for rol in roles:
        Users_rols.add(user.id, rol)
    flash("Insercion exitosa", "success")

    return redirect(url_for("user_index"))


def update(user_id):
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así a partir de un usuario en particular muestra la información previamente cargada en
    la creación del mismo

    """
    if not authenticated(session):
        abort(401)
    if not has_permit('user_update'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    user = User.with_id(user_id)
    rols = Rol.except_rols(user.roles())

    return render_template("user/update.html", user=user, rols=rols)


def update_new():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así obtiene los nuevos datos cargados en el formulario y realiza la actualización del mismo
    realizando previamente las validaciones correspondientes a los datos ingresados.
    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_update'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    data = request.form
    if not form_user_update(data):
        return redirect(request.referrer)

    data = request.form
    if not form_user_update(data):
        return redirect(request.referrer)

    user = User.with_id(data['user_id'])
    if exist_email_update(data['email'], user.email):
        return redirect(request.referrer)

    if exist_username_update(data['username'], user.username):
        return redirect(request.referrer)

    dictUser = {}

    dictUser = {
        "username": bleach.clean(data['username']),
        "first_name": bleach.clean(data['first_name']),
        "last_name": bleach.clean(data['last_name']),
        "email": bleach.clean(data['email'])
    }

    user.update(dictUser)
    flash("Actualización exitosa.", "success")

    return redirect(url_for('user_index'))


def delete():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así elimina al usuario seleccionado.
    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_destroy'):
        flash("No posee permisos.", "danger")
        return redirect(url_for("home"))

    user = User.with_id(request.form['user_id'])
    user.delete()
    flash("Eliminación exitosa.", "success")

    return redirect(url_for('user_index'))


def search():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así pagina el listado de usuarios de acuerdo a los elementos almacenados en la configuración,
    mostrando los usuarios de ayuda que coincidan con la opción de búsqueda ingresada y/o seleccionada

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_index'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    estado = request.args.get("estado")
    filter = request.args.get("filtro")

    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    if estado == '---':
        users = User.with_filter(filter).paginate(page,
                                                  per_page,
                                                  error_out=False)
        return render_template("user/index.html", users=users, estado=estado)

    if estado == 'activo':
        users = User.active_with_filter(filter).paginate(page,
                                                         per_page,
                                                         error_out=False)
        return render_template("user/index.html", users=users, estado=estado)

    users = User.deactive_with_filter(filter).paginate(page,
                                                       per_page,
                                                       error_out=False)

    return render_template("user/index.html", users=users, estado=estado)


def show(user_id):
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así a partir de un usuario en particular muestra los datos del mismo.

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_show'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    user = User.with_id(user_id)

    return render_template("user/show.html", user=user)


def perfil():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así a partir de un usuario en particular muestra los datos del mismo.

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_perfil'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    user = User.with_username(session["username"])
    return render_template("user/show.html", user=user)


def activated(user_id):
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así a partir de un usuario en particular si el mismo esta desactivado lo activa y viceversa.

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_update'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    user = User.with_id(user_id)
    if is_admin(user):
        flash("El admin no puede ser deshabilitado", "danger")
        return redirect(url_for('user_index'))

    if user.is_active():
        user.deactivate()
    else:
        user.activate()

    return redirect(url_for('user_index'))


def configuracion():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así obtengo los datos de la configuración y configuro la web.

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_update'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    configuracion = db.session.query(Config).first()
    form = ConfigForm()

    return render_template("config/configuracion.html",
                           config=configuracion,
                           form=form)


def rol_delete():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así elimino el rol seleccionado.

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_update'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    data = request.args
    user_rol = Users_rols.with_userid_rolid(data)
    user_rol.delete()
    flash("Rol eliminado correctamente", "success")

    return redirect(request.referrer)


def add_rols():
    """
    Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
    de ser así agrega el rol seleccionado.

    """
    if not authenticated(session):
        abort(401)

    if not has_permit('user_update'):
        flash("No posee permisos", "danger")
        return redirect(url_for("home"))

    user_id = request.args['user_id']
    roles = request.form.getlist('roles[]')
    for rol in roles:
        Users_rols.add(user_id, rol)

    flash("Insercion exitosa", "success")

    return redirect(request.referrer)
