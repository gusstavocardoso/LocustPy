from flask import Blueprint, jsonify, request

album_api = Blueprint('album_api', __name__)

albums = []

@album_api.route('/albums', methods=['GET'])
def get_albums():
    return jsonify(albums)

@album_api.route('/albums', methods=['POST'])
def create_album():
    data = request.json
    albums.append(data)
    return jsonify({"message": "Album created successfully"}), 201
