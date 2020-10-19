from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection

from app.models.user import User
from app.models.config import Config

from app import db


def login():
    return render_template("auth/login.html")

def authenticate():
    """ Este metodo realiza la autenticacion de un usuario,
    teniendo en cuenta si los datos ingresados en el formulario
    son correctos, si el usuario se encuntra o no activo,
    y si la pagina está o no habilitada
    """
    user = db.session.query(User).filter(User.email == request.form['email']).filter(User.password == request.form['password']).first()
    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))
    if not Config.getConfig().is_active():
        if not user.has_permit("login_when_desactivated"):
            flash("El sitio se encuentra en mantenimiento")
            return redirect(url_for("home"))
    session["user"] = user.email
    session["username"] = user.username
    flash("La sesión se inició correctamente.")
    return redirect(url_for("home"))

def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")
    return redirect(url_for("auth_login"))
