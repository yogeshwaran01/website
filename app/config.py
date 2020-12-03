import os

class Configaration:
    SECRET_KEY = "mywebsiteuseflaskapp"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "cerulean"
    BASIC_AUTH_USERNAME = os.environ.get('ADMIN_USER')
    BASIC_AUTH_PASSWORD = os.environ.get('ADMIN_PASS')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
