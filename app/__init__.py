from os import path, environ
from flask import Flask, render_template, g
from flask_session import Session
from config import config
from app.db import db
from app.resources import user
from app.resources import auth
from app.resources import centro
from app.resources import turno
from app.resources import config as configuracion
from app.helpers import handler
from app.helpers import auth as helper_auth
from flask_sqlalchemy import SQLAlchemy
from app.models.config import Config
from app.models.user import User
from app.helpers.permits import has_permit, is_admin
from flask_bootstrap import Bootstrap
from flask import jsonify
from app.resources.api import centros
from flask_googlemaps import GoogleMaps


db = SQLAlchemy()

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)


    api_key = 'AIzaSyCLV1EU7HG-O5I9HEoSXY1XuRA9iXPITGE' # change this to your api key
    GoogleMaps(app, key=api_key)

    Bootstrap(app)
    app.config['SECRET_KEY'] = 'ThisIsAVerySecretKey'
    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    # Configure db

    db.init_app(app)

   # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated,has_permit=has_permit,is_admin=is_admin)

    # Autenticación    A DONDE ME LLEVA  NOM DE LA VISTA  LA FUNCION DEL RECURSO A EJECUTAR
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])


    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/update/<user_id>", "user_update", user.update)
    app.add_url_rule("/usuarios/show/<user_id>", "user_show", user.show)
    app.add_url_rule("/usuarios/update", "user_update_new", user.update_new, methods=["POST"])
    app.add_url_rule("/usuarios/delete", "user_delete", user.delete, methods=["POST"])
    app.add_url_rule("/usuarios/search", "user_search", user.search)
    app.add_url_rule("/usuarios/index/<user_id>", "user_activated", user.activated, methods=["POST"])
    app.add_url_rule("/configuracion", "user_configuracion", user.configuracion)
    app.add_url_rule("/perfil", "user_perfil", user.perfil)
    app.add_url_rule("/usuarios/update/user_delete_rol", "user_rol_delete", user.rol_delete, methods=["POST"])
    app.add_url_rule("/usuarios/update/user_add_rols", "user_add_rols", user.add_rols, methods=["POST"])

    # Rutas de turnos un centro en particular
    app.add_url_rule("/centros/turnos/index/<centro_id>", "turno_index", turno.index)
    app.add_url_rule("/centros/turnos/nuevo/create", "turno_create", turno.create, methods=["POST"])
    app.add_url_rule("/centros/turnos/index/<centro_id>/nuevo", "turno_new", turno.new)
    app.add_url_rule("/centros/turnos/update/<turno_id>", "turno_update", turno.update)
    app.add_url_rule("/centros/turnos/update", "turno_update_new", turno.update_new, methods=["POST"])
    app.add_url_rule("/centros/turnos/delete", "turno_delete", turno.delete, methods=["POST"])
    app.add_url_rule("/centros/turnos/show/<turno_id>", "turno_show", turno.show)
    app.add_url_rule("/centros/turnos/search/<centro_id>", "turno_search", turno.search)

    #Rutas de todos los turnos
    app.add_url_rule("/turnos", "turno_index_all", turno.index)
    app.add_url_rule("/turnos/show/<turno_id>", "turno_show_all", turno.show)
    app.add_url_rule("/centros/turnos/search", "turno_search_all", turno.search)
    app.add_url_rule("/turnos/nuevo", "turno_new_all", turno.new)

    # Rutas de Centros
    app.add_url_rule("/centros", "centro_index", centro.index)
    app.add_url_rule("/centros", "centro_create", centro.create, methods=["POST"])
    app.add_url_rule("/centros/nuevo", "centro_new", centro.new)
    app.add_url_rule("/centros/show/<centro_id>", "centro_show", centro.show)
    app.add_url_rule("/centros/delete", "centro_delete", centro.delete, methods=["POST"])
    app.add_url_rule("/centros/update/<centro_id>", "centro_update", centro.update)
    app.add_url_rule("/centros/update", "centro_update_new", centro.update_new, methods=["POST"])
    app.add_url_rule("/centros/search", "centro_search", centro.search)

    #Rutas de configuracion
    app.add_url_rule("/configuracion", "config_update", configuracion.update, methods=["POST"])

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        configuracion = Config.getConfig()
        sitio_activo = configuracion.is_active()
        if sitio_activo:
            return render_template("home.html", config=configuracion)
        return render_template("mantenimiento.html")

    # Ruta para la api con el listado de centros
    @app.route('/centros')
    def getCentros():
        return jsonify(centros)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500 y 401

    # Retornar la instancia de app configurada
    return app
