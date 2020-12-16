from application import app, db
from application.models import User, Post
from flask import render_template

@app.route('/')
def home():
    test = ['it','works', 'times 10', '!!!']
    return render_template('index.html', test = test)

@app.route('/add')
def add():
    new_post = Post(detail="First app post")
    db.session.add(new_post)
    db.session.commit()
    return "new post"

@app.route('/read')
def read():
    all_posts = Post.query.all()
    post_string = ""
    for post in all_posts:
        post_string += "<br>" + post.detail 
    return post_string

