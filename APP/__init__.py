from flask import Flask
from flask_cors import CORS
from .controllers import product_bp
from .db import init_db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    init_db(app)

    app.register_blueprint(product_bp, url_prefix='/api')

    return app
