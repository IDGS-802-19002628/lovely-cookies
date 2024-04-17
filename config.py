import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

class Config(object):
    SECRET_KEY='CLAVE SECRETA'
    SESSION_COOKIE_SECURE=False
    @staticmethod
    def init_app(app):
        pass

class DevelomentConfig(Config):
    DEBUG=True
    usuario = os.getenv("DB_USERNAME")
    pwd = os.getenv("DB_PASSWORD")
    DB = os.getenv("DB")
    DB_H = os.getenv("DB_HOST")
    print(usuario)
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{usuario}:{pwd}@{DB_H}/{DB}"
    
db = SQLAlchemy()