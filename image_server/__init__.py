from flask import Flask
from image_server import file, image
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config['STORAGE_PATH'] = '/home/malte.fillmer/images'

    jwt = JWTManager(app)

    app.register_blueprint(file.bp, url_prefix="/file")
    app.register_blueprint(image.bp, url_prefix="/image")

    return app
