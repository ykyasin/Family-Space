from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired, Optional
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
        name = name.data.lower()
        if not name.isalpha(): 
            raise ValidationError("Must only contain letters")
        if len(name) < 2 or len(name) > 20:
                raise ValidationError("Name has to be between 2 and 20 characters")
        for taken_user in taken_users:
            if name == taken_user.name.lower(): 
                raise ValidationError("Name already taken, please choose another")
        

class PostForm(FlaskForm):
    detail = StringField('How you feeling?', validators=[
        Length(max=120, message="Must be less than 120 characters"),
        Optional()
    ])
    postid = HiddenField()
    submit = SubmitField('Post')
    submit2 = SubmitField('Delete')
    submit3 = SubmitField('Delete your account')
    yesdel = SubmitField('Yes')
    nodel = SubmitField('No')
    chname_button = SubmitField('Change account name')
    chname = StringField('Input name', validators=[
        Optional(strip_whitespace=False)
    ])
    submit4 = SubmitField('Change')
    submit5 = SubmitField('Logout')

    def validate_chname(self, chname):
        taken_users = User.query.all()
        chname = chname.data.lower()
        if not chname.isalpha(): 
            raise ValidationError("Must only contain letters")
        if len(chname) < 2 or len(chname) > 20:
                raise ValidationError("Name has to be between 2 and 20 characters")
        for taken_user in taken_users:
            if chname == taken_user.name.lower(): 
                raise ValidationError("Name already taken, please choose another")
    

class AddUser(FlaskForm):
    submit = SubmitField('Add User')