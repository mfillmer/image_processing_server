from flask import jsonify, current_app
from json import loads, dumps
from time import time
import os


def get_identity_file(owner):
    storage = current_app.config['STORAGE_PATH']
    metadir = os.path.join(storage, '.meta')
    identity_file = os.path.join(metadir, owner)
    if not os.path.exists(metadir):
        os.mkdir(metadir)
    return identity_file


def store_file_metadata(filename, owner):
    id_file = get_identity_file(owner)
    try:
        data = open(id_file).read()
    except Exception:
        data = ""

    if data is "":
        data = '{}'
    meta_data = loads(data)
    meta_data[filename] = {
        'name': filename,
        'created_at': int(time())
    }
    with open(get_identity_file(owner), 'w+') as file:
        file.write(dumps(meta_data))
    return meta_data


def delete_file_metadata(file, owner):
    id_file = get_identity_file(owner)
    try:
        data = open(id_file).read()
    except Exception:
        data = ""

    if data is "":
        data = '{}'
    meta_data = loads(data)
    del meta_data[filename]

    with open(get_identity_file(owner), 'w+') as file:
        file.write(dumps(meta_data))
    return meta_data
