from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired
from application.models import User

def  choice_user():
    return User.query

class Login(FlaskForm):
    users = QuerySelectField(query_factory=choice_user, allow_blank=False, get_label='name')
    submit = SubmitField('Login')

class UserForm(FlaskForm):
    name = StringField('Name', validators=[
        InputRequired(),
        Length(min=2, max=20)
    ])
    submit = SubmitField('Add new member')

    def validate_name(self, name):
        taken_users = User.query.all()
        for taken_user in taken_users:
            if name.data.lower() == taken_user.name.lower(): 
                raise ValidationError("Name already taken, please choose another")
        

class PostForm(FlaskForm):
    detail = StringField('How you feeling?', validators=[
        DataRequired(),
        Length(min=5, max=180, message="not right")
    ])
    post = HiddenField()
    submit = SubmitField('Post')
    submit2 = SubmitField('Delete')
    submit3 = SubmitField('Delete your account')
    yesdel = SubmitField('Yes')
    nodel = SubmitField('No')
    chname_button = SubmitField('Change account name')
    chname = StringField('Input name', validators=[
        DataRequired(),
        Length(min=2, max=20)
    ])
    submit4 = SubmitField('Change')
    submit5 = SubmitField('Logout')
    

class AddUser(FlaskForm):
    submit = SubmitField('Add User')