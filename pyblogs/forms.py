import flask_wtf
import wtforms
from wtforms import validators as valid
import string





def domain_check(form,field):
    mail = field.data
    if not mail.endswith("@gmail.com"):
        raise wtforms.ValidationError('email has to end with G-mail')


class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField('User Name:', validators=[valid.Length(max=12),valid.DataRequired(message="Username cant be empty")])
    email    = wtforms.StringField('Email:', validators=[domain_check,valid.DataRequired(), valid.Email()])
    password = wtforms.PasswordField('Password', validators=[valid.DataRequired(), valid.Length(min=8)])
    password_confirmation = wtforms.PasswordField('Confirm', validators= [valid.DataRequired(),valid.EqualTo('password')])
    submit   = wtforms.SubmitField('Sign Up')


class SigninForm(flask_wtf.FlaskForm):

    username = wtforms.StringField('User Name:')

    password = wtforms.PasswordField('password')


    submit = wtforms.SubmitField('Sign In')