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

from flask import request

@views.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.pizza.price * item.quantity for item in cart_items)
    address = None
    if request.method == 'POST':
        address = request.form.get('address')
        if not address or len(address) < 5:
            flash('Please enter a valid delivery address.', 'error')
            return render_template('checkout.html', cart_items=cart_items, total=total, address=address)
        # Store address in session for order placement
        session['address'] = address
        return redirect(url_for('views.place_order'))
    return render_template('checkout.html', cart_items=cart_items, total=total, address=address)






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

from flask import request, redirect, url_for
from .models import  Order, OrderItem, Pizza
from flask_login import current_user

@views.route('/place-order', methods=['POST', 'GET'])
@login_required
def place_order():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash("Your cart is empty.", "error")
        return redirect(url_for('views.my_cart'))
    address = session.get('address')
    if not address:
        flash("Please provide a delivery address.", "error")
        return redirect(url_for('views.checkout'))
    # Create the order
    new_order = Order(user_id=current_user.id)
    db.session.add(new_order)
    db.session.flush()
    # Add items to order
    for item in cart_items:
        order_item = OrderItem(
            order_id=new_order.id,
            pizza_id=item.pizza_id,
            quantity=item.quantity
        )
        db.session.add(order_item)
    # Store address in order (add address field if not present)
    new_order.address = address
    # Clear the cart after order
    CartItem.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    session.pop('address', None)
    flash("Your order has been placed successfully!", "success")
    return redirect(url_for('views.order_confirmation', order_id=new_order.id))





