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
                    if name = "user_new":
                        return redirect(url_for('user/index.html'))
                        #if usr.rol = "Operador":
                            #Mejorar
                        






                user = User.query.get(usr.id)
                if not user or not user.active or not user.has_permit(permit):
                    flash(PERMIT_ERROR, 'danger')
                    if not user.active:
                        return redirect(url_for('welcome'))
                    if user and user.has_permit('admin_index'):
                        return redirect(url_for('admin_index'))
                    else:
                        return redirect(url_for('welcome'))
                else:
                    return controller(*args, **kwargs)
            else:
                return redirect(url_for('auth_login'))
        return wrapper

    return decorate_view


# def permits_enabled(permit):
#     """recibe un nombre de permiso y un usuario, si el usuario no tiene el permiso lo redirige al welcome"""

#     def decorate_view(controller):

#         @wraps(controller)
#         def wrapper(*args, **kwargs):
#             user = session.get('user')
#             if not user or not user.has_permit(permit):
#                 flash(PERMIT_ERROR, 'danger')
#                 if user and user.has_role('OPERADOR'):
#                     return redirect(url_for('admin_index'))

#                 return redirect(url_for('welcome'))
#             else:
#                 return controller(*args, **kwargs)
#         return wrapper

#     return decorate_view



def profile_permits(permit, current_user):
    """wrapper para la funcion perfil(user_id) recibe un nombre de permiso y el usuario actual,
    ademas usa el parametro user_id de la funcion perfil,
    si el usuario actual no tiene la misma ID, o si no tiene permiso, es enviado al welcome"""

    def decorate_view(controller):

        @wraps(permits_enabled)
        def wrapper(*args, **kwargs):
            user_id = kwargs.get('user_id')
            if user_id == str(current_user.id):
                return controller(*args, **kwargs)
            else:
                permits = permits_enabled(permit, current_user)
                return permits(controller)(*args, **kwargs)
        return wrapper

    return decorate_view
