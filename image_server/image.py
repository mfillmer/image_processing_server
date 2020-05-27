from flask import Blueprint, current_app, jsonify, make_response, request
from json import loads
from image_server.meta import get_identity_file
from image_server.file import find_file
from PIL import Image
import io

bp = Blueprint(__name__, __name__)


def make_response_from_image(img):
    if type(img) is not Image.Image:
        raise(TypeError('Must be type PIL.Image.Image'))
    output = io.BytesIO()
    img.save(output, format='JPEG')

    response = make_response(output.getvalue())
    response.headers.set('Content-Type', 'image/jpeg')
    return response


@bp.route('/')
def list_owners_files():
    owner = 'mock'
    path = get_identity_file(owner)
    if path is None:
        return 'file not found', 404
    return jsonify(loads(open(path, 'r').read()))


@bp.route('/<file>')
def serve_file(file):
    path = find_file(file)
    if path is None:
        return 'file not found', 404

    img = Image.open(path)

    rot = request.values.get('rotation', 0)
    img = img.rotate(int(rot))

    size = request.values.get('size', '')
    if size is not None:  # regex
        size = tuple([int(x) for x in size.split(',')])
    img.thumbnail(size)

    return make_response_from_image(img)
