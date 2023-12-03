import secrets, os
from PIL import Image
from wtforms.validators import ValidationError
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user,\
    login_required
from carrent import app, db, bcrypt
from carrent.forms import SignUpForm, LoginForm, UpdateAccountForm,\
    PostCarForm, ReservationForm, PostOwnerForm
from carrent.models.user import User
from carrent.models.car import Car
from carrent.models.owner import Owner
from carrent.models.reservation import Reservation


@app.route("/sign-up", methods=['GET', 'POST'], strict_slashes=False)
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
        return redirect(url_for('login'))
    return render_template('sign-up.html', title='Sign-up', form=form)

@app.route("/login", methods=['GET', 'POST'], strict_slashes=False)
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
    cars = Car.query.all()
    owners = Owner.query.all()
    return render_template('home.html', title='Homepage', cars=cars, owners=owners)

@app.route("/logout", strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('login'))

def save_pic(form_pic):
    """Saving the user profile picture"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_pic.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static/profile_pics', pic_fn)

    output_size = (250,250)
    img = Image.open(form_pic)
    img.thumbnail(output_size)
    img.save(pic_path)

    return pic_fn

@app.route("/account",  methods=['GET', 'POST'], strict_slashes=False)
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.pic.data:
            pic_file = save_pic(form.pic.data)
            current_user.img_file = pic_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    img_file = url_for('static', filename='profile_pics/' + current_user.img_file)
    return render_template('account.html', title='Account',
                           img_file=img_file, form=form )

def save_car_pic(car_pic):
    """Saving the user profile picture"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(car_pic.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static/car_images', pic_fn)
    car_pic.save(pic_path)
    return pic_fn

@app.route("/car/new", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def new_car():
    if current_user.username == 'Safuan':
        form = PostCarForm()
        if form.validate_on_submit():
            if form.pic.data:
                pic_file = save_car_pic(form.pic.data)
            owner_name = form.car_owner.data
            owner = Owner.query.filter_by(name=owner_name).first()
            car = Car(make = form.make.data,
                    model = form.model.data,
                    year = form.year.data,
                    description = form.description.data,
                    Seating = form.seating.data,
                    daily_price = form.daily_price.data,
                    car_owner = owner,
                    img_file = pic_file
                    )
            db.session.add(car)
            db.session.commit()
            flash('You car has been posted', 'success')
            return redirect(url_for('home'))
        return render_template('post_car.html', title='New Car', form=form)
    else:
        return redirect(url_for('home'))

@app.route("/car/<int:car_id>/update", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def update_car(car_id):
    if current_user.username == 'Safuan':
        car = Car.query.get_or_404(car_id)
        form = PostCarForm()
        if form.validate_on_submit():
            if form.pic.data:
                pic_file = save_car_pic(form.pic.data)
                car.img_file = pic_file
            car.make = form.make.data
            car.model = form.model.data
            car.year = form.year.data
            car.Seating = form.seating.data
            car.description = form.description.data
            car.daily_price = form.daily_price.data
            db.session.commit()
            flash('Your car has been updated!', 'success')
            return redirect(url_for('home'))
        elif request.method == "GET":
            form.make.data = car.make
            form.model.data = car.model
            form.year.data = car.year
            form.seating.data = car.Seating
            form.description.data = car.description
            form.daily_price.data = car.daily_price
            form.car_owner.data = car.car_owner.name
        return render_template('post_car.html', title='Car Update', car=car, form=form)
    else:
        return redirect(url_for('home'))

@app.route("/reservation/<int:car_id>", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def reservation(car_id):
    car = Car.query.get_or_404(car_id)
    owners = Owner.query.all()
    form = ReservationForm()

    if form.validate_on_submit():
        form.car_id = car_id
        try:
            form.validate_reservation()
            reservation = Reservation(start_date=form.start_date.data,
                                    end_date=form.end_date.data,
                                    car_id=car.id,
                                    user_id=current_user.id,
                                    owner_id=car.car_owner.id)
            db.session.add(reservation)
            db.session.commit()
            flash('Your booking has completed', 'success')
            return redirect(url_for('home'))
        except ValidationError as e:
            flash(str(e), 'danger')
            return render_template('reservation.html',
                                   title=car.make + '.' + car.model,
                                   car=car, form=form, owners=owners)
    return render_template('reservation.html',
                           title=car.make + '.' + car.model,
                           car=car, form=form, owners = owners)

@app.route("/owner/<int:owner_id>", strict_slashes=False)
def owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    return render_template('owner.html', titel=owner.name, owner=owner)

@app.route("/owner/new", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def new_owner():
    """"""
    if current_user.username == 'Safuan':
        form = PostOwnerForm()
        if form.validate_on_submit():
            owner = Owner(name=form.name.data, address=form.address.data)
            db.session.add(owner)
            db.session.commit()
            flash('Owner successfully created!', 'success')
            return redirect(url_for('home'))
        return render_template('post_owner.html', title='New Provider', form=form)
    else:
        return redirect(url_for('home'))

@app.route("/about", strict_slashes=False)
def about():
    return render_template('about.html', title='About Us')

@app.route("/owners", strict_slashes=False)
def owners():
    owners = Owner.query.all()
    return render_template('owners.html', title='Providers', owners=owners)
