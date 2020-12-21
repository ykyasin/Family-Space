from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import User

def  choice_user():
    return User.query

class Login(FlaskForm):
    users = QuerySelectField(query_factory=choice_user, allow_blank=True, get_label='name')

class UserForm(FlaskForm):
    name = StringField('Input name')
    submit = SubmitField('Add User')

class PostForm(FlaskForm):
    detail = StringField('How you feeling? ')
    submit = SubmitField('Post')