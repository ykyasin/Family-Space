from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import User

def  choice_user():
    return User.query

class Login(FlaskForm):
    users = QuerySelectField(query_factory=choice_user, allow_blank=False, get_label='name')
    submit = SubmitField('Login')

class UserForm(FlaskForm):
    name = StringField('Input name')
    submit = SubmitField('Add User')

class PostForm(FlaskForm):
    detail = StringField('How you feeling? ')
    submit = SubmitField('Post')
    submit2 = SubmitField("Click here to delete your account")
    submit3 = SubmitField("Delete")

class AddUser(FlaskForm):
    submit = SubmitField("Add User")

class DelUser(FlaskForm):
    submit = SubmitField("Click here to delete your account")

class DelPost(FlaskForm):
    post = HiddenField()
    submit = SubmitField("Delete")
