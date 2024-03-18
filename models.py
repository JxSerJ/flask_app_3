from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

