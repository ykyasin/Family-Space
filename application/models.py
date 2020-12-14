from application import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    surname = db.Column(db.String(30))

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(180))