import os
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SECRET_KEY='CLAVE SECRETA'
    SESSION_COOKIE_SECURE=False
    @staticmethod
    def init_app(app):
        pass

class DevelomentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://admin:Guanajuato2001@127.0.0.1/lovely_cookies'
    
db = SQLAlchemy()