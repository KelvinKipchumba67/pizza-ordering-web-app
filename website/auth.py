from flask import Blueprint,render_template
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

auth = Blueprint('auth',__name__)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username= request.form.get('username')
        password=request.form.get('password')


        user=User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')

                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Username does not exist', category='error')

     

    return render_template("login.html", user=current_user)

@auth.route('/logout')
def logout():
    return "<P>Logout</p>"


@auth.route ('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists.')
            return redirect(url_for('auth.login'))
        new_user=User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! Please login.')
        return redirect (url_for('auth.login'))
    return render_template("signup.html")