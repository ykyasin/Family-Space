from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UserForm(FlaskForm):
    name = StringField('Input name')
    submit = SubmitField('Add User')