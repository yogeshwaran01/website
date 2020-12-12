import os


class Configaration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "cerulean"
    BASIC_AUTH_USERNAME = os.environ.get('ADMIN_USER')
    BASIC_AUTH_PASSWORD = os.environ.get('ADMIN_PASS')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    UPLOAD_FOLDER = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py', 'js'}
