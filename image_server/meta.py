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


def store_file_metadata(filename, owner, **kwargs):
    id_file = get_identity_file(owner)

    try:
        data = open(id_file).read()
    except Exception:
        data = ""

    if data == "":
        data = '{}'
    meta_data = loads(data)
    meta_data_item = {
        'name': filename,
        'created_at': int(time()),
        **kwargs
    }
    meta_data[filename] = meta_data_item
    with open(get_identity_file(owner), 'w+') as file:
        file.write(dumps(meta_data))
    return meta_data_item


def delete_file_metadata(file, owner):
    id_file = get_identity_file(owner)
    try:
        data = open(id_file).read()
    except Exception:
        data = ""

    if data == "":
        data = '{}'
    meta_data = loads(data)
    del meta_data[file]

    with open(get_identity_file(owner), 'w+') as file:
        file.write(dumps(meta_data))
    return meta_data
