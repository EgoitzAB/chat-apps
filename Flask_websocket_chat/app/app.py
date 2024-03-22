from flask import Flask
from config import Config
from flask_login import LoginManager
from .routes import auth as auth_blueprint
from .routes import chat as chat_blueprint
from .routes import main as main_blueprint
from extensions import db, socketio
from flask_redis import FlaskRedis
from .models.user import User
from flask_migrate import Migrate


login_manager = LoginManager()
redis_store = FlaskRedis()
migrate = Migrate()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)
    redis_store.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_blueprint.auth)
    app.register_blueprint(chat_blueprint.chat)
    app.register_blueprint(main_blueprint.main)

    return app