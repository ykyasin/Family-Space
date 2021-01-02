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
    post = HiddenField()
    submit = SubmitField('Post')
    submit2 = SubmitField('Delete')
    submit3 = SubmitField('Click here to delete your account')
    chname_button = SubmitField('Click here to change account name')
    chname = StringField('Input name')
    submit4 = SubmitField('Change')
    

class AddUser(FlaskForm):
    submit = SubmitField('Add User')