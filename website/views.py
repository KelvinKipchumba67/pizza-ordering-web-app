# where the routes are stored 
from flask import Blueprint,render_template,session,redirect,flash
from flask import *
from flask_login import current_user, login_required
from . import db  
from .models import Pizza, CartItem
from sqlalchemy.orm import joinedload

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

# @views.route('/cart')
# @login_required
# def my_cart():
#     return render_template("cart.html")

@views.route('/menu')
def menu():
    return render_template("menu.html")

@views.route ('/checkout')
def checkout():
    return "<p>This is the checkout</p>"






@views.route('/add_to_cart/<int:pizza_id>')
@login_required
def add_to_cart(pizza_id):
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        flash("Pizza not found.", "error")
        return redirect(url_for('views.my_cart'))

    # check if already in cart
    item = CartItem.query.filter_by(user_id=current_user.id, pizza_id=pizza_id).first()
    if item:
        item.quantity += 1
    else:
        new_item = CartItem(user_id=current_user.id, pizza_id=pizza_id, quantity=1)
        db.session.add(new_item)

    db.session.commit()
    flash(f"Added {pizza.name} to your cart!", "success")
    return redirect(url_for('views.my_cart'))


@views.route('/cart')
@login_required
def my_cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.pizza.price * item.quantity for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)

@views.route('/remove_from_cart/<int:item_id>')
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        flash(f"Removed {item.pizza.name} from your cart.", "info")
    else:
        flash("Item not found in your cart.", "error")
    return redirect(url_for('views.my_cart'))



