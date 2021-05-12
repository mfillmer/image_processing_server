from image_server.util import restore_orientation
from PIL import Image
from flask import Blueprint, request, jsonify, render_template, current_app
from image_server.meta import store_file_metadata, delete_file_metadata
from flask_jwt_extended import jwt_required, get_jwt_identity
import uuid
import os

bp = Blueprint(__name__, __name__)


def find_file(file):
    store = current_app.config['STORAGE_PATH']
    path = os.path.join(store, file)

    if os.path.exists(path):
        return path

    return None


@bp.route('/')
def serve_form():
    return render_template('upload.html')


@bp.route('/', methods=['POST'])
@jwt_required()
def create_file():
    store = current_app.config['STORAGE_PATH']
    filename = str(uuid.uuid4())
    meta = store_file_metadata(filename, get_jwt_identity())
    if 'file' not in request.files:
        return 'no file found', 400
    file = request.files['file']
    image = Image.open(file)
    image = restore_orientation(image)

    image.save(os.path.join(store, filename), 'jpeg')
    image.close()

    return jsonify(meta[filename]), 201


@bp.route('/<file>', methods=['DELETE'])
@jwt_required()
def delete_file(file):
    store = current_app.config['STORAGE_PATH']
    meta = delete_file_metadata(file, get_jwt_identity())
    os.remove(os.path.join(store, file))
    return jsonify(meta), 200
