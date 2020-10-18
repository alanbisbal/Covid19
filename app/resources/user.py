from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection

from app.models.user import User
from app.models.rol import Rol

from app.models.users_rols import Users_rols
from app.helpers.auth import authenticated

from app import db
from app.models.config import Config

# protected resources
def index():
    if not authenticated(session):
        abort(401)
    # retorna todos los usuarios
    users = User.all()
    users_permits = User.permit_recovery(users)
    return render_template("user/index.html", users=users, users_permits = users_permits)
    return render_template("home.html")

def new():
    if not authenticated(session):
        abort(401)
    rols = Rol.all()
    # retorna vista de creacion de usuario
    return render_template("user/new.html",rols=rols)

def create():
    if not authenticated(session):
        abort(401)
    # validaciones de acceso administrador
    data = request.form
    # validacion de campos unicos
    user_with_email = User.with_email(data['email'])
    if user_with_email:
        flash("El email ya existe en el sistema.")
        return redirect(request.referrer)
    user_with_username = User.with_username(data['username'])
    if user_with_username:
        flash("El nombre de usuario ya existe en el sistema.")
        return redirect(request.referrer)
    # insercion a la base de datos
    User.add(data)
    user = User.with_email(data['email'])
    Users_rols.add(user.id,data['rol'])
    flash("Insercion exitosa")
    return redirect(url_for("user_index"))

def update(user_id):
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    # retorna una vista con el id del usuario enviado por parametro
    print (user.permit_recovery())
    return render_template("user/update.html", user=user)

def update_new():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    data = request.form
    # Se controla los campos unicos.
    user = User.with_id(data['user_id'])
    user_with_email = User.with_email(data['email'])
    user_with_username = User.with_username(data['username'])
    if user_with_email and user_with_email.id != user.id:
        flash("El email ya existe en el sistema.")
        return redirect(request.referrer)
    if user_with_username and user_with_username.id != user.id:
        flash("El nombre de usuario ya existe en el sistema.")
        return redirect(request.referrer)
    # actualiza el usuario
    user.update(data)
    flash("Actualizacion exitosa.")
    return redirect(url_for('user_index'))

def delete():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    # se busca el usuario en la base de datos y se lo elimina
    user = User.with_id(request.form['user_id'])
    user.delete()
    return redirect(url_for('user_index'))

def search():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    estado = request.args.get("estado")
    filter = request.args.get("filtro")
    # se aplica filtro independientemente del estado
    if estado == '---':
        users = User.with_filter(filter)
        return render_template("user/index.html", users=users)
    # se aplica filtro con estado activo
    if estado == 'activo':
        users = User.active_with_filter(filter)
        return render_template("user/index.html", users=users)
    # se aplica filtro con estado inactivo
    users = User.deactive_with_filter(filter)
    return render_template("user/index.html", users=users)

def show(user_id):
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador y si lo es retorna el usuario enviado por id
    user = User.with_id(user_id)
    return render_template("user/show.html",user = user)
    # validacion de acceso de usuario a su propio perfil y si lo es, retorna su perfil
    # --completar para futura entrega--

def activated(user_id):
    if not authenticated(session):
        abort(401)
    user = User.with_id(user_id)
    if user.active():
        user.deactivate()
    else:
        user.activate()
    return redirect(url_for('user_index'))

def configuracion():
    if not authenticated(session):
        abort(401)
    # validacion de acceso administrador
    # retorna una vista con el id del usuario enviado por parametro
    configuracion = db.session.query(Config).first()
    return render_template("config/configuracion.html", config=configuracion)
