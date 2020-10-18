from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection
from app.models.user import User
from app.models.rol import Rol
from app.models.users_rols import Users_rols
from app.helpers.auth import authenticated
from app import db
from app.models.config import Config
from app.helpers.validates import form_user_new,exist_email,exist_username,form_user_update,exist_email_update,exist_username_update
from app.helpers.permits import has_permit


# Protected resources
def index():
    if not authenticated(session):
        abort(401)
    if not has_permit('user_index'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    #retorna todos los usuarios
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    users = User.query.paginate(page,per_page,error_out=False)
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)
    if not has_permit('user_new'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    rols = Rol.all()
    #retorna vista de creacion de usuario
    return render_template("user/new.html",rols=rols)


def create():
    if not authenticated(session):
        abort(401)
    if not has_permit('user_new'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    #validaciones de acceso administrador
    data = request.form
    if not form_user_new(data):
        return redirect(request.referrer)
    if exist_email(data['email']):
        return redirect(request.referrer)
    if exist_username(data['username']):
        return redirect(request.referrer)
    #insercion a la base de datos
    User.add(data)
    user = User.with_email(data['email'])
    Users_rols.add(user.id,data['rol'])
    flash("Insercion exitosa")
    return redirect(url_for("user_index"))



def update(user_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('user_update'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    #validacion de acceso administrador

    #retorna una vista con el id del usuario enviado por parametro
    user = User.with_id(user_id)
    return render_template("user/update.html",user = user)



def update_new():
    if not authenticated(session):
        abort(401)
    if not has_permit('user_update'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    #validacion de acceso administrador

    data = request.form
    if not form_user_update(data):
        return redirect(request.referrer)
    #Se controla los campos unicos.
    data = request.form
    if not form_user_update(data):
        return redirect(request.referrer)
    user = User.with_id(data['user_id'])
    if exist_email_update(data['email'],user.email):
        return redirect(request.referrer)
    if exist_username_update(data['username'],user.username):
        return redirect(request.referrer)
    user.update(data)
    flash("Actualizacion exitosa.")
    return redirect(url_for('user_index'))



def delete():
    if not authenticated(session):
        abort(401)
    #validacion de acceso administrador
    if not has_permit('user_destroy'):
        flash("No posee permisos.")
        return redirect(url_for("home"))
    #se busca el usuario en la base de datos y se lo elimina
    user = User.with_id(request.form['user_id'])
    user.delete()
    return redirect(url_for('user_index'))

def search():
    if not authenticated(session):
        abort(401)
    #validacion de acceso administrador
    if not has_permit('user_index'):
        flash("No posee permisos")
        return redirect(url_for("home"))

    estado = request.args.get("estado")
    filter = request.args.get("filtro")
    # se aplica filtro independientemente del estado
    per_page = Config.getConfig().elementos
    page = request.args.get("page", 1, type=int)
    if estado == '---':
        users = User.with_filter(filter).paginate(page,per_page,error_out=False)
        return render_template("user/index.html", users=users)
    # se aplica filtro con estado activo
    if estado == 'activo':
        users = User.active_with_filter(filter).paginate(page,per_page,error_out=False)
        return render_template("user/index.html", users=users)
    # se aplica filtro con estado inactivo
    users = User.deactive_with_filter(filter).paginate(page,per_page,error_out=False)
    return render_template("user/index.html", users=users)


def show(user_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('user_show'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    #validacion de acceso administrador y si lo es retorna el usuario enviado por id
    user = User.with_id(user_id)
    return render_template("user/show.html",user = user)
    #validacion de acceso de usuario a su propio perfil y si lo es, retorna su perfil
    #---completar para futura entrega--#

def activated(user_id):
    if not authenticated(session):
        abort(401)
    if not has_permit('user_update'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    user = User.with_id(user_id)
    if user.is_active():
        user.deactivate()
    else:
        user.activate()
    return redirect(url_for('user_index'))


def configuracion():
    if not authenticated(session):
        abort(401)
    if not has_permit('user_update'):
        flash("No posee permisos")
        return redirect(url_for("home"))
    #validacion de acceso administrador

    #retorna una vista con el id del usuario enviado por parametro
    configuracion = db.session.query(Config).first()
    return render_template("config/configuracion.html", config=configuracion)