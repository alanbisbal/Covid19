from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.user import User


def validate_form_user(data):
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
        return True
    else:
        return False
