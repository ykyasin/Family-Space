from application import app, db
from application.models import User
from flask import render_template

@app.route('/')
def home():
    return 'nothing to see'

@app.route('/read')
def check():
    user = User.query.order_by(User.id).all()
    return str(user[1].name)

@app.route('/add/<name>')
def add(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f'New User added: {user.name}'



