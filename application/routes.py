from application import app, db
from application.models import User, Post
from application.forms import UserForm, PostForm, Login, AddUser, ChNameForm, DelAccForm
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
@app.route('/main')
def home():
    return redirect(url_for('login'))

@app.route('/main/<user>', methods = ['GET','POST'])
def main(user):
    postform = PostForm()
    chnameform = ChNameForm()
    delaccform = DelAccForm()
    name_change = False
    delete_account = True
    post_db = Post.query.order_by(Post.id).all()
    posts = []
    posts_id = []
    post_time = []
    users = []
    for i in reversed(range(len(post_db))):
        posts.append(post_db[i].detail)
        posts_id.append(post_db[i].id)
        post_time.append(post_db[i].date_time)
        users.append(post_db[i].user.name)


    if request.method == 'POST':

        if delaccform.delacc_button:
            delete_account = True
            return render_template('index.html', delaccform=delaccform, chnameform=chnameform, postform = postform, posts=posts, user=user, post_time=post_time, users=users, posts_id=posts_id, name_change=name_change, delete_account=delete_account)
        
        if delaccform.yes_del:
           return "yes"
        
        if delaccform.no_del.data:
            delete_account = False
            return redirect(url_for('main', user=user))

        if chnameform.validate_on_submit:
            if chnameform.chname_button.data: 
                name_change = True
                return render_template('index.html', delaccform=delaccform, chnameform=chnameform, postform = postform, posts=posts, user=user, post_time=post_time, users=users, posts_id=posts_id, name_change=name_change, delete_account=delete_account)

            if chnameform.submit.data:
                newname = postform.chname.data
                olduser = User.query.filter_by(name=user).first()
                olduser.name = newname
                db.session.commit()
                user = newname
                name_change_session = False
        if chnameform.errors: 
            return str(chnameform.errors)

        if postform.validate_on_submit():

            if postform.submit5.data:
                return redirect(url_for('login'))

            if postform.submit.data:
                post = postform.detail.data
                new_post = Post(detail=post, user = User.query.filter_by(name=user).first())
                #User.query.filter_by(name=user).first()
                db.session.add(new_post)
                db.session.commit()
                
            
            if postform.submit2.data: 
                postid = postform.post.data
                dcpost = Post.query.filter_by(id=postid).first()
                db.session.delete(dcpost)
                db.session.commit()
            
            return redirect(url_for('main', user=user))

    return render_template('index.html', delaccform=delaccform, chnameform=chnameform, postform = postform, posts=posts, user=user, post_time=post_time, users=users, posts_id=posts_id, name_change=name_change, delete_account=delete_account)

@app.route('/login', methods = ['GET','POST'])
def login(): #Add users
    form = Login()
    formuser= UserForm()
    if len(User.query.all()) == 0:
        are_users = False
    else: 
        are_users = True

    if request.method == 'POST':
        if formuser.name.data and formuser.validate_on_submit():
            name = formuser.name.data
            newuser = User(name=name)
            db.session.add(newuser)
            db.session.commit()
            return redirect(url_for('login'))
        elif formuser.name.data:
            return render_template('login.html', form = form, formuser = formuser, are_users=are_users)
        else:
            user = form.users.data
            return redirect(url_for('main', user=user.name))

    return render_template('login.html', form = form, formuser = formuser, are_users=are_users)






