from application import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    posts = db.relationship('Post', backref='user') 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(180))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #, nullable=False)