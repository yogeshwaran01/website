from flask import Flask, Response, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_simplemde import SimpleMDE

from .config import Configaration

# init Flask app
app = Flask(__name__)
app.config.from_object(Configaration)

# init Database for Flask app
database = SQLAlchemy(app)
migrate = Migrate(app, db=database)
SimpleMDE(app)

# Setup for Admin page to interact with database
admin = Admin(app, name="Admin", template_mode="bootstrap3")
auth = BasicAuth(app)

from app import views
