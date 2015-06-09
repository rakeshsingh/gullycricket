from gullycricket import app
from flask import jsonify, make_response, abort, request
players = [
    {
        "name": "Rakesh Singh",
        "dob": 1981,
        "id": 1,
        "role": "Batsman"
    }, {
        "name": "Utkarsh Khare",
        "dob": 1981,
        "id": 2,
        "role": "Batsman"
        }
]


@app.route('/gullycricket/api/v1.0/players', methods=['GET'])
def get_players():
    return jsonify({'players': players})


@app.route('/gullycricket/api/v1.0/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    return jsonify({'player': player[0]})


@app.route('/gullycricket/api/v1.0/players', methods=['POST'])
def create_player():
    if not request.json or 'name' not in request.json:
        abort(400)
    player = {
        'id': players[-1]['id'] + 1,
        'name': request.json['name'],
        'dob': request.json.get('dob', ""),
        'role': 'Batsman'
    }
    players.append(player)
    return jsonify({'player': player}), 201


@app.route('/gullycricket/api/v1.0/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'role' in request.json and type(request.json['role']) is not bool:
        abort(400)
    player[0]['name'] = request.json.get('name', player[0]['name'])
    player[0]['dob'] = request.json.get('dob', player[0]['dob'])
    player[0]['role'] = request.json.get('role', player[0]['role'])
    return jsonify({'player': player[0]})


@app.route('/gullycricket/api/v1.0/players/<int:player_id>',
           methods=['DELETE'])
def delete_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    players.remove(player[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
