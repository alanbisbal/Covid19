from flask import redirect, render_template, request, url_for, session, abort, flash
from app import db

from app.models.config import Config
from app.helpers.auth import authenticated

from app.helpers.forms import ConfigForm


def update():
    """
     Este método verifica si el usuario esta logueado y tiene permisos para estar en esa sección,
     de ser así obtiene los nuevos datos ingresados en el formulario y actualiza su información .

    """
    if not authenticated(session):
        abort(401)
    config = Config.getConfig()
    form = ConfigForm(old_elmentos=config.cant_elements)
    if not form.validate_on_submit():
        return redirect(request.referrer)
    config.update(request.form)
    flash("actualizacion exitosa", "success")
    return redirect(url_for('user_configuracion'))
