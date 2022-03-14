import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    

    SECRET_KEY = 'b\x08h(\xbfe\xb9\x11\x89\xc7m\x85PQo0\xca\xd8\xea-\x7f\x84\xe8F'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


    #email configurations

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kojwangbora254@gmail.com'
    MAIL_PASSWORD = 'tiktaktu'


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   
    pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}