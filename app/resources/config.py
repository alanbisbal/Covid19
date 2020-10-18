from flask import redirect, render_template, request, url_for, session, abort, flash
from app import db

from app.models.config import Config
from app.helpers.auth import authenticated


def update():
    if not authenticated(session):
        abort(401)
    config = Config.getConfig()
    config.update(request.form)
    flash("actualizacion exitosa")
    return redirect(url_for('user_configuracion', config = config))
