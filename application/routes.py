from application import app, db
from application.models import User, Post
from application.forms import UserForm, PostForm, Login, AddUser
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('login'))

@app.route('/main/<user>', methods = ['GET','POST'])
def main(user = "No User"):
    postform = PostForm()
    if request.method == 'POST':
        post = postform.detail.data
        new_post = Post(detail=post, user=user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main'))
    post_db = Post.query.order_by(Post.id).all()
    posts = []
    for i in range(len(post_db)):
        posts.append(post_db[i])
    return render_template('index.html', postform = postform, posts=posts, user=user)

@app.route('/login', methods = ['GET','POST'])
def login(): #Add users
    form = Login()
    formuser= UserForm()
    if request.method == 'POST':
        if formuser.name.data:
            name = formuser.name.data
            newuser = User(name=name)
            db.session.add(newuser)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            user = form.users.data
            return redirect(url_for('main', user=user.name))

    return render_template('login.html', form = form, formuser = formuser)

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


