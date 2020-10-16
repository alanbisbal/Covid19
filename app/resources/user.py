from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection
from app.models.user import User
from app.helpers.auth import authenticated
from app import db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)
    #retorna todos los usuarios
    users = db.session.query(User).all()
    return render_template("user/index.html", users=users)
    return render_template("home.html")


def new():
    if not authenticated(session):
        abort(401)
    #retorna vista de creacion de usuario
    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)

    #validaciones de acceso administrador
    data = request.form
    #validacion de campos unicos
    user_with_email = db.session.query(User).filter_by(email = data['email']).first()
    user_with_username = db.session.query(User).filter_by(username = data['username']).first()
    if user_with_email:
        flash("El email ya existe en el sistema.")
        return redirect(request.referrer)
    if user_with_username:
        flash("El nombre de usuario ya existe en el sistema.")
        return redirect(request.referrer)
    #insercion a la base de datos.
    db.add(User(data))
    db.commit()
    flash("Insercion exitosa")
    return redirect(url_for("user_index"))



def update(user_id):
    if not authenticated(session):
        abort(401)
    #validacion de acceso administrador

    #retorna una vista con el id del usuario enviado por parametro
    user = db.session.query(User).filter_by(id= user_id).first()
    return render_template("user/update.html",user = user)



def update_new():
    if not authenticated(session):
        abort(401)
    #validacion de acceso administrador

    data = request.form
    #Se controla los campos unicos.
    user = db.session.query(User).get(data['user_id'])


    """
    test sobre que permisos tiene el usuario
    for rol in user.rols:
        for permiso in rol.permisos:
            print(permiso.name)
    """


    user_with_email = db.session.query(User).filter_by(email = data['email']).first()
    user_with_username = db.session.query(User).filter_by(username = data['username']).first()
    if user_with_email and user_with_email.id != user.id:
        flash("El email ya existe en el sistema.")
        return redirect(request.referrer)
    if user_with_username and user_with_username.id != user.id:
        flash("El nombre de usuario ya existe en el sistema.")
        return redirect(request.referrer)
    #actualiza el usuario
    if user.first_name != data['first_name']:
        user.first_name = data['first_name']
    if user.username != data['username']:
        user.username = data['username']
    if user.last_name != data['last_name']:
        user.last_name = data['last_name']
    if user.email != data['email']:
        user.email = data['email']
    db.session.commit()
    flash("Actualizacion exitosa.")
    return redirect(url_for('user_index'))



def delete():
    if not authenticated(session):
        abort(401)
    #validacion de acceso administrador

    #se busca el usuario en la base de datos y se lo elimina
    user = db.session.query(User).get(request.form['user_id'])
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_index'))

def search():
    if not authenticated(session):
        abort(401)
    #validacion de acceso administrador

    estado = request.args.get("estado")
    filtro = request.args.get("filtro")
    # se aplica filtro independientemente del estado
    if estado == '---':
        users = db.session.query(User).filter(User.username.contains(filtro))
        return render_template("user/index.html", users=users)
    # se aplica filtro con estado activo
    if estado == 'activo':
        users = db.session.query(User).filter(User.activo == True,User.username.contains(filtro))
        return render_template("user/index.html", users=users)
    # se aplica filtro con estado inactivo
    users = db.session.query(User).filter(User.activo == False).filter(User.username.contains(filtro))
    return render_template("user/index.html", users=users)


def show(user_id):
    if not authenticated(session):
        abort(401)
    #validacion de acceso administrador y si lo es retorna el usuario enviado por id
    user = db.session.query(User).filter_by(id= user_id).first()
    return render_template("user/show.html",user = user)
    #validacion de acceso de usuario a su propio perfil y si lo es, retorna su perfil
    #---completar para futura entrega--#
