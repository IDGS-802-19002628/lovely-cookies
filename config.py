import os
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from encriptar_config import desencriptador


class Config(object):
    SECRET_KEY='CLAVE SECRETA'
    SESSION_COOKIE_SECURE=False
    @staticmethod
    def init_app(app):
        pass

class DevelomentConfig(Config):
    DEBUG=True
    
    SQLALCHEMY_DATABASE_URI=desencriptador
    
db = SQLAlchemy()