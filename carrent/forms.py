"""Importing necessary modules"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from carrent.models.user import User

class SignUpForm(FlaskForm):
    """This is the signup from class"""
    username = StringField('Username', 
                           validators=[DataRequired(), length(min=4, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), length(min=4)])
    confirm_password = PasswordField('Confirm password',
                             validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username used. Please choose another one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email used. Please choose another one')

class LoginForm(FlaskForm):
    """This is the signup from class"""
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')
