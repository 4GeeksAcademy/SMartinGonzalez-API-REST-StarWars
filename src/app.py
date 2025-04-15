"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Starships
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def get_all_users():
    users_query = User.query.all()

    response_body = {
        "msg": "Succes",
        "results": list(map(lambda user: user.serialize(), users_query)),
        "total_users": len(users_query)
    }

    return jsonify(response_body), 200


@app.route('/characters', methods=['GET'])
def get_all_characters():
    characters_query = Characters.query.all()

    response_body = {
        "msg": "Success",
        "results": list(map(lambda character: character.serialize(), characters_query)),
        "total_characters": len(characters_query)
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets_query = Planets.query.all()

    response_body = {
        "msg": "Success",
        "results": list(map(lambda planet: planet.serialize(), planets_query)),
        "total_planets": len(planets_query)
    }

    return jsonify(response_body), 200


@app.route('/starships', methods=['GET'])
def get_all_starships():
    starships_query = Starships.query.all()

    response_body = {
        "msg": "Success",
        "results": list(map(lambda starship: starship.serialize(), starships_query)),
        "total_planets": len(starships_query)
    }

    return jsonify(response_body), 200


@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Characters.query.filter_by(char_id=character_id).first()

    if not character:
        return jsonify({"msg": "Character not found"}), 404

    response_body = {
        "msg": "Success",
        "result": character.serialize()
    }

    return jsonify(response_body), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.filter_by(pla_id=planet_id).first()

    if not planet:
        return jsonify({"msg": "Planet not found"}), 404

    response_body = {
        "msg": "Success",
        "result": planet.serialize()
    }

    return jsonify(response_body), 200

@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_starship(starship_id):
    starship = Starships.query.filter_by(ship_id=starship_id).first()

    if not starship:
        return jsonify({"msg": "Starship not found"}), 404

    response_body = {
        "msg": "Success",
        "result": starship.serialize()
    }

    return jsonify(response_body), 200

@app.route('/user/char_favorites/<int:user_id>', methods=['GET'])
def get_char_favorites(user_id):
    user = User.query.get(user_id)
    fav_chars = []

    if not user:
        return jsonify({"msg": "Starship not found"}), 404
    
    for favorite in user.char_favorites:
        fav_chars.append(favorite.character.serialize())

    return jsonify({'favorites': fav_chars})

@app.route('/user/planet_favorites/<int:user_id>', methods=['GET'])
def get_planet_favorites(user_id):
    user = User.query.get(user_id)
    fav_planets = []

    if not user:
        return jsonify({"msg": "Starship not found"}), 404
    
    for favorite in user.pla_favorites:
        fav_planets.append(favorite.planet.serialize())

    return jsonify({'favorites': fav_planets})

@app.route('/user/ship_favorites/<int:user_id>', methods=['GET'])
def get_ship_favorites(user_id):
    user = User.query.get(user_id)
    fav_ships = []

    if not user:
        return jsonify({"msg": "Starship not found"}), 404
    
    for favorite in user.ship_favorites:
        fav_ships.append(favorite.starship.serialize())

    return jsonify({'favorites': fav_ships})

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
