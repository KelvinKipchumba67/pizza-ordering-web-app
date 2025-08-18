from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db=SQLAlchemy()
DB_NAME = "database.db"
login_manager=LoginManager()


# function creating the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='abvjfjfdjdhfhhffdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"



    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view ='auth.login'

    from .views import views
    from .auth import auth

    # registering the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()
        if not Pizza.query.first():  # only add if DB is empty
            pizzas = [
                Pizza(name="Tuna", price=800),
                Pizza(name="Pepperoni", price=950),
                Pizza(name="Four Cheese", price=1000),
                Pizza(name="Margherita", price=750),
                Pizza(name="Hawaiian", price=850),
                Pizza(name="Mushroom", price=780),
            ]
            db.session.add_all(pizzas)
            db.session.commit()
            print("✅ Pizzas added to the database!")
                  
        else:
            print("⚠️ Pizzas already exist")
    





    return app
 
from .models import User,Pizza, CartItem, Order, OrderItem 


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))


