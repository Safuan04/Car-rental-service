"""Importing necessary modules"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from datetime import datetime
from wtforms import StringField, PasswordField, SubmitField, BooleanField,\
    IntegerField, TextAreaField, FloatField, DateField
from wtforms.validators import DataRequired, length, Email, EqualTo,\
    ValidationError
from carrent.models.user import User
from carrent.models.owner import Owner
from carrent.models.reservation import Reservation


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

class UpdateAccountForm(FlaskForm):
    """This is the UpdateAccount from class"""
    username = StringField('Username', 
                           validators=[DataRequired(), length(min=4, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    pic = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username used. Please choose another one')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email used. Please choose another one')
            
class PostCarForm(FlaskForm):
    """This is the PostCar form class"""
    car_owner = StringField('car owner', validators=[DataRequired()])
    make = StringField('make', validators=[DataRequired()])
    model = StringField('model', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()], default=2015)
    description = TextAreaField('desciption', validators=[DataRequired()])
    daily_price = FloatField('daily_price', validators=[DataRequired()])
    pic = FileField('Car picture', validators=[DataRequired(), FileAllowed(['jpeg', 'jpg', 'png'])])
    submit = SubmitField('Post')

    def validate_car_owner(self, car_owner):
        car_owner = Owner.query.filter_by(name=car_owner.data).first()
        if not car_owner:
            raise ValidationError("Owner doesn't exists")

class ReservationForm(FlaskForm):
    """This is the Reservation form class"""
    start_date = DateField('From', validators=[DataRequired()], default=datetime.utcnow())
    end_date = DateField('To', validators=[DataRequired()], default=datetime.utcnow())
    submit = SubmitField('Book')

    def validate_reservation(self):
        start_date = self.start_date.data
        end_date = self.end_date.data

        if start_date and end_date:
            conflicting_reservations = Reservation.query.filter(
                Reservation.car_id == self.car_id,
                Reservation.start_date <= end_date,
                Reservation.end_date >= start_date
            ).all()

            if conflicting_reservations:
                raise ValidationError('This car is not available for the selected dates. Please choose different dates.')
