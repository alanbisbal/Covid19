from flask import redirect, url_for, flash, session
from functools import wraps
from app.models.user import User

PERMIT_ERROR = 'No tiene permisos para acceder a esa sección. \
Contacte con un administrador.'

#estas funciones son wrappers, se las llama poniendo @nombre_funcion antes de una funciona a la
#que uno quiera que se apliquen
#ejemplo:
#@profile_permissions('user_index', current_user)
#def profile(user_id):

def permits_enabled(permit):
    """recibe un nombre de permiso y un usuario, si el usuario no tiene el permiso lo redirige al welcome"""

    def decorate_view(controller):

        @wraps(controller)
        def wrapper(*args, **kwargs):
            usr = session.get('user')
            if usr:
                perm_array[]= usr.permit_recovery()
                for n in perm_array:
                    if perm_array.name = "user_new":
                        return redirect(url_for('user/index.html'))
                        
