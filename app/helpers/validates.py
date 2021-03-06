from flask import redirect, render_template, request, url_for, session, abort, flash
import requests
import bleach
from app.models.user import User
from app.helpers.upload import upload_pdf
import datetime
<<<<<<< HEAD
 
=======

>>>>>>> 8575660b5a51118cb48d5860bb7bc0a1b3c07c86
def form_user_new(data):
    ok = True
    if not data['username']:
        flash('El nombre de usuario no puede estar vacio', "danger")
        ok = False
    if not data['first_name']:
        flash('El nombre no puede estar vacio', "danger")
        ok = False
    if not data['last_name']:
        flash('El apellido no puede estar vacio', "danger")
        ok = False
    if not data['email']:
        flash('El email no puede estar vacio', "danger")
        ok = False
    if not data['password']:
        flash('La contraseña no puede estar vacia', "danger")
        ok = False
    if not data['activo']:
        flash('El estado no puede estar vacio', "danger")
    if ok:
        return True
    else:
        return False


def exist_email(data):
    user = User.with_email(data)
    if user:
        flash("El email ya existe en el sistema.", "danger")
        return True
    else:
        return False


def exist_username(data):
    user = User.with_username(data)
    if user:
        flash("El nombre de usuario ya existe en el sistema.", "danger")
        return True
    else:
        return False


def exist_email_update(data, email):
    if data != email:
        user = User.with_email(data)
        if user:
            flash("El email ya existe en el sistema.", "danger")
            return True
        else:
            return False
    return False


def exist_username_update(data, username):
    if data != username:
        user = User.with_username(data)
        if user:
            flash("El nombre de usuario ya existe en el sistema.", "danger")
            return True
        else:
            return False
    return False


def form_user_update(data):
    ok = True
    if not data['username']:
        flash('El nombre de usuario no puede estar vacio', "danger")
        ok = False
    if not data['first_name']:
        flash('El nombre no puede estar vacio', "danger")
        ok = False
    if not data['last_name']:
        flash('El apellido no puede estar vacio', "danger")
        ok = False
    if not data['email']:
        flash('El email no puede estar vacio', "danger")
        ok = False
    if ok:
        return True
    else:
        return False


def form_config_update(data):
    ok = True
    if not data['titulo']:
        flash('El titulo no puede estar vacio', "danger")
<<<<<<< HEAD
        ok = False
    if not data['descripcion']:
        flash('La descripcion no puede estar vacio', "danger")
=======
        ok = False
    if not data['descripcion']:
        flash('La descripcion no puede estar vacio', "danger")
        ok = False
    if not data['email']:
        flash('El email no puede estar vacio', "danger")
>>>>>>> 8575660b5a51118cb48d5860bb7bc0a1b3c07c86
        ok = False
    if ok:
        return True
    else:
        return False


def form_turno(data):
    ok = True
    if not data['email']:
        flash('El email no puede estar vacio', "danger")
<<<<<<< HEAD
=======
        ok = False
    if not data['bloque']:
        flash('El horario no puede estar vacio', "danger")
        ok = False
    if not data['fecha']:
        flash('La fecha no puede estar vacia', "danger")
>>>>>>> 8575660b5a51118cb48d5860bb7bc0a1b3c07c86
        ok = False
    if ok:
        return True
    else:
        return False


<<<<<<< HEAD
def form_turno(data):
    ok = True
    if not data['email']:
        flash('El email no puede estar vacio', "danger")
        ok = False
    if not data['bloque']:
        flash('El horario no puede estar vacio', "danger")
        ok = False
    if not data['fecha']:
        flash('La fecha no puede estar vacia', "danger")
        ok = False
    if ok:
        return True
    else:
        return False


=======
>>>>>>> 8575660b5a51118cb48d5860bb7bc0a1b3c07c86
def validar_municipio(data):
    municipios = requests.get(
        "https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios"
    ).json()['data']['Town']
    for mun in municipios:
        if (str(municipios[mun]["id"]) == data):
            return True
    return False

def sanitizar_input(form):
    for i in form.data:
        if not isinstance(form[i].data, (int, str, float, datetime.time)):
            continue
        else:
            if form[i].data is None:
                continue
        form[i].data= bleach.clean(str(form[i].data))
