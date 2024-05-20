from flask import Flask
from flask_cors import CORS
from .controllers import product_bp
from .db import init_db
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
   # Configuración de la carpeta de subida de imágenes
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    CORS(app)
    init_db(app)

    app.register_blueprint(product_bp, url_prefix='/api')

    return app
