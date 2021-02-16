import os


class Configuration:
    """ Configurations for Flask app """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "cerulean"
    BASIC_AUTH_USERNAME = os.environ.get('ADMIN_USER')
    BASIC_AUTH_PASSWORD = os.environ.get('ADMIN_PASS')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
