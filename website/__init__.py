from flask import Flask

# function creating the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='abvjfjfdjdhfhhffdf'

    from .views import views
    from .auth import auth

    # registering the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app

