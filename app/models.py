from app import database as db

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.title} -> {self.timestamp}"


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    message = db.Column(db.Text())

    def __repr__(self):
        return f"{self.name} -> {self.email}"
