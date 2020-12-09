from app import database as db

from datetime import datetime


class Posts(db.Model):
    """" Database Table for Blog post """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.title} -> {self.timestamp}"


class Contact(db.Model):
    """" Database Table for Contact details """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    message = db.Column(db.Text())

    def __repr__(self) -> str:
        return f"{self.name} -> {self.email}"


class Portfolio(db.Model):
    """" Database Table for portfolio """

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())

    def __repr__(self) -> str:
        return f"{self.id}"
