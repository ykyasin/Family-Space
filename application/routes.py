from application import app, db
from application.models import User
from application.forms import UserForm
from flask import Flask, render_template, request

@app.route('/')
def home():
    return 'nothing to see'

@app.route('/read')
def check():
    user = User.query.order_by(User.id).all()
    names = []
    for i in range(len(user)):
        names.append(user[i].name)

    return str(names)

@app.route('/add/<name>')
def add(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f'New User added: {user.name}' 

@app.route('/user', methods = ['GET','POST'])
def userform():
    userform = UserForm()
    if request == 'POST':
        name = userform.name.data
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return "Added"
    
    return render_template('name.html', userform = userform)


