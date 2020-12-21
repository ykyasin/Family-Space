from application import app, db
from application.models import User, Post
from application.forms import UserForm, PostForm
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
def home():
    postform = PostForm()
    if request.method == 'POST':
        post = postform.name.data
        user = Post(post=post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('check'))
    post_db = Post.query.order_by(Post.id).all()
    posts = []
    for i in range(len(post_db)):
        posts.append(post_db[i].detail)
    return render_template('index.html', postform = postform, posts=posts)

@app.route('/read')
def check():
    user = User.query.order_by(User.id).all()
    users = []
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
    if request.method == 'POST':
        name = userform.name.data
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('check'))
    
    return render_template('name.html', userform = userform)


