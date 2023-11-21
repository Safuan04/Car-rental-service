from flask import render_template, url_for, flash, redirect, request
from carrent.forms import SignUpForm, LoginForm
from carrent.models.user import User
from carrent.models.car import Car
from carrent.models.owner import Owner
from carrent.models.reservation import Reservation
from carrent import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/sign-up", methods=['GET', 'POST'],strict_slashes=False)
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Hi {form.username.data}, your account has been created! You can now log in', 'success')
        return redirect(url_for('home'))
    return render_template('sign-up.html', title='Sign-up', form=form)

@app.route("/login", methods=['GET', 'POST'],strict_slashes=False)
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
             flash('login unsuccessful, Please check your email and password', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route("/", strict_slashes=False)
@app.route("/home", strict_slashes=False)
def home():
    return render_template('home.html', title='Homepage',)

@app.route("/logout", strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account", strict_slashes=False)
@login_required
def account():
    return render_template('account.html', title='Account')
