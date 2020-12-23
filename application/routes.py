from application import app, db
from application.models import User, Post
from application.forms import UserForm, PostForm, Login
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('login'))

@app.route('/main', methods = ['GET','POST'])
def main():
    postform = PostForm()
    if request.method == 'POST':
        post = postform.detail.data
        new_post = Post(detail=post)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main'))
    post_db = Post.query.order_by(Post.id).all()
    posts = []
    for i in range(len(post_db)):
        posts.append(post_db[i].detail)
    return render_template('index.html', postform = postform, posts=posts)

@app.route('/login', methods = ['GET','POST'])
def login(): #Add users
    form = Login()
    return render_template('login.html', form = form)

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
        return redirect(url_for('home'))
    
    return render_template('name.html', userform = userform)


