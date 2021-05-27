from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_simplemde import SimpleMDE
from flask_compress import Compress
from flask_cors import CORS

from .config import Configuration

# init Flask app
app = Flask(__name__)
# loads configuration for flask app
app.config.from_object(Configuration)

Compress(app)
CORS(app)

# init Database for Flask app
database = SQLAlchemy(app)
migrate = Migrate(app, db=database)
SimpleMDE(app)

# Setup for Admin page to interact with database
admin = Admin(app, name="Admin", template_mode="bootstrap3")
auth = BasicAuth(app)

from app import views
