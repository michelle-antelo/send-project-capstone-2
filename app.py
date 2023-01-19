import os

from flask import Flask, render_template, request, session, g, redirect, jsonify, flash
from sqlalchemy.exc import IntegrityError
from flask_restful import Api, Resource

from models import db, connect_db, User
from forms import UserAddForm, LoginForm


CURR_USER_KEY = "curr_user"

DATABASE_URL = "postgresql:///send_project"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")

app.app_context().push()

connect_db(app)

# db.create_all()

##############################################################################
#User/Admin signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None

def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Sign up user and redirect to home page"""

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data.lower(),
                name=form.name.data,
                password=form.password.data,
                email=form.email.data.lower(),
                image_url=form.image_url.data or User.image_url.default.arg,
                bio=form.bio.data,
                user_type=form.user_type.data,
            )
            
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('signup.html', form=form)

        do_login(user)

        flash(f"Hello, {user.username}!", "success")
        return redirect("/")

    else:
        return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """Logout user"""

    do_logout()

    flash("Successfully logged out!", "success")
    return redirect("/")

##############################################################################
#Render Homepage

@app.route('/')
def homepage():

    if CURR_USER_KEY in session:
        return render_template("home.html")

    else: 
        return render_template("welcome.html")