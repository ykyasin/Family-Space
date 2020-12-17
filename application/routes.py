from application import app, db
from application.models import User
from flask import render_template

@app.route('/')
def home():
    return 'nothing to see'

@app.route('/name')
def check(name):
    user = User.query.filter_by(name=name).first()
    return f'user: {user.location}'

@app.route('/<name>')
def add(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return "new user added"



