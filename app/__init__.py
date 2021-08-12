from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.calculate_distance import bp as distance_bp
    app.register_blueprint(distance_bp)

    return app