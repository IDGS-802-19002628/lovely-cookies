import os
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SECRET_KEY='CLAVE SECRETA'
    SESSION_COOKIE_SECURE=False

class DevelomentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:12345@127.0.0.1/don_galleto'

db = SQLAlchemy()