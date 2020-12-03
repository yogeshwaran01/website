from flask import Flask, Response, redirect
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_simplemde import SimpleMDE

from .config import Configaration

app = Flask(__name__)
app.config.from_object(Configaration)

database = SQLAlchemy(app)
migrate = Migrate(app, db=database)
SimpleMDE(app)

admin = Admin(app, name="Admin", template_mode="bootstrap3")
auth = BasicAuth(app)

from app import views
