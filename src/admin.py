import os
from flask_admin import Admin
from models import db, User, Characters, Planets, Starships, CharacterFavorites, PlanetFavorites, StarshipFavorites
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import class_mapper, RelationshipProperty


class UserModelView(ModelView):
    column_auto_select_related = True  # Carga automáticamente las relaciones
    # Columnas y relationships de mi tabla PeopleFavorites
    column_list = ['id', 'name', 'lastname', 'email', 'password', 'is_active', 'char_favorites', 'pla_favorites', 'ship_favorites']

class CharactersModelView(ModelView):
    column_auto_select_related = True  # Carga automáticamente las relaciones
    # Columnas y relationships de mi tabla PeopleFavorites
    column_list = ['char_id', 'char_name', 'gender', 'race', 'height', 'allegiance', 'favorite_by']

class PlanetsModelView(ModelView):
    column_auto_select_related = True  # Carga automáticamente las relaciones
    # Columnas y relationships de mi tabla PeopleFavorites
    column_list = ['pla_id', 'pla_name', 'system', 'moons','favorite_by']

class StarshipsModelView(ModelView):
    column_auto_select_related = True  # Carga automáticamente las relaciones
    # Columnas y relationships de mi tabla PeopleFavorites
    column_list = ['ship_id', 'ship_name', 'designer', 'affiliation','year_introduced','favorite_by']    

class CharacterFavoritesModelView(ModelView):
    column_auto_select_related = True  # Carga automáticamente las relaciones
    # Columnas y relationships de mi tabla PeopleFavorites
    column_list = ['id', 'user_id', 'user', 'character_id','character']

class PlanetFavoritesModelView(ModelView):
    column_auto_select_related = True  # Carga automáticamente las relaciones
    # Columnas y relationships de mi tabla PeopleFavorites
    column_list = ['id', 'user_id', 'user', 'planet_id','planet']

class StarshipFavoritesModelView(ModelView):
    column_auto_select_related = True  # Carga automáticamente las relaciones
    # Columnas y relationships de mi tabla PeopleFavorites
    column_list = ['id', 'user_id', 'user', 'starship_id','starship']         


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(CharactersModelView(Characters, db.session))
    admin.add_view(PlanetsModelView(Planets, db.session))
    admin.add_view(StarshipsModelView(Starships, db.session))
    admin.add_view(CharacterFavoritesModelView(CharacterFavorites, db.session))
    admin.add_view(PlanetFavoritesModelView(PlanetFavorites, db.session))
    admin.add_view(StarshipFavoritesModelView(StarshipFavorites, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))