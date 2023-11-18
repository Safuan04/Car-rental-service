from flask import render_template, url_for, flash, redirect
from carrent.forms import SignUpForm, LoginForm
from carrent import app

@app.route("/sign-up", methods=['GET', 'POST'],strict_slashes=False)
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('sign-up.html', title='Sign-up', form=form)

@app.route("/login", methods=['GET', 'POST'],strict_slashes=False)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'safuan.elmail@gmail.com' and form.password.data == '123456app':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful, Please check your email and password', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route("/", strict_slashes=False)
@app.route("/home", strict_slashes=False)
def home():
    return render_template('home.html', title='Homepage',)
