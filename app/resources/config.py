from flask import redirect, render_template, request, url_for, session, abort, flash
from app import db

from app.models.config import Config
from app.helpers.auth import authenticated

from app.helpers.validates import form_config_update


def update():
    if not authenticated(session):
        abort(401)
    if form_config_update(request.form):
        config = Config.getConfig()
        config.update(request.form)
        flash("actualizacion exitosa")
        return redirect(url_for('user_configuracion', config=config))
    return redirect(request.referrer)
