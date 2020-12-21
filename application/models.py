from application import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(180))