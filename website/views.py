# where the routes are stored 
from flask import Blueprint,render_template,session


views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/cart')
def my_cart():
    return render_template("cart.html")

@views.route('/menu')
def menu():
    return render_template("menu.html")

@views.route ('/checkout')
def checkout():
    return "<p>This is the checkout</p>"


