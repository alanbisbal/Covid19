from app import db
from flask import request

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import permiso, user, users_rols, rols_permisos


    @classmethod
    def __str__(self):
        return '<Rol {}>'.format(self.name)

    def all():
        return db.session.query(Rol).all()

    def permission_names(self):
        return [permiso.name for permiso in self.permisos]

    def has_permit(self, permit_name):
        """ Obtiene los permisos y devuelve un boolean
        respecto al nombre del permisos que se paso por parametro """
        permits = map(lambda p: p.name == permit_name, self.permisos)
        return any(permits)
