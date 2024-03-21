from flask import Flask
from config import Config
from flask_login import LoginManager
from .routes import auth as auth_blueprint
from .routes import chat as chat_blueprint
from extensions import db, socketio
from flask_redis import FlaskRedis

login_manager = LoginManager()
redis_store = FlaskRedis()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)
    redis_store.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(chat_blueprint)
    return app