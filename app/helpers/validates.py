from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.user import User


def form_user_new(data):
    ok = True
    if not data['username']:
        flash('El nombre de usuario no puede estar vacio')
        ok = False
    if not data['first_name']:
        flash('El nombre no puede estar vacio')
        ok = False
    if not data['last_name']:
        flash('El apellido no puede estar vacio')
        ok = False
    if not data['email']:
        flash('El email no puede estar vacio')
        ok = False
    if not data['password']:
        flash('La contraseña no puede estar vacia')
        ok = False
    if ok:
        return True
    else:
        return False


def exist_email(data):
    user = User.with_email(data)
    if user:
        flash("El email ya existe en el sistema.")
        return True
    else:
        return False

def exist_username(data):
    user = User.with_username(data)
    if user:
        flash("El nombre de usuario ya existe en el sistema.")
        return True
    else:
        return False

def exist_email_update(data,email):
    if data != email:
        user = User.with_email(data)
        if user:
            flash("El email ya existe en el sistema.")
            return True
        else:
            return False
    return False

def exist_username_update(data,username):
    if data != username:
        user = User.with_username(data)
        if user:
            flash("El nombre de usuario ya existe en el sistema.")
            return True
        else:
            return False
    return False

def form_user_update(data):
    ok = True
    if not data['username']:
        flash('El nombre de usuario no puede estar vacio')
        ok = False
    if not data['first_name']:
        flash('El nombre no puede estar vacio')
        ok = False
    if not data['last_name']:
        flash('El apellido no puede estar vacio')
        ok = False
    if not data['email']:
        flash('El email no puede estar vacio')
        ok = False
    if ok:
        return True
    else:
        return False

def form_config_update(data):
    ok = True
    if not data['titulo']:
        flash('El titulo no puede estar vacio')
        ok = False
    if not data['description']:
        flash('La descripcion no puede estar vacio')
        ok = False
    if not data['email']:
        flash('El email no puede estar vacio')
        ok = False
    if ok:
        return True
    else:
        return False
