from flask import redirect, url_for, flash, session
from app.models.user import User
from app.models.rol import Rol
from app.models.permiso import Permiso

def has_permit(permit):
    user = User.with_username(session['username'])
    for rol in user.rols:
        for permiso in rol.permisos:
            if(permit == permiso.name):
                return True
    return False
