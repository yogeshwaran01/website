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
