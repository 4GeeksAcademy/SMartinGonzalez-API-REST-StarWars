from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__= 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    lastname: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    char_favorites: Mapped[list['CharacterFavorites']] = relationship(back_populates='user', cascade='all, delete-orphan')
    pla_favorites: Mapped[list['PlanetFavorites']] = relationship(back_populates='user', cascade='all, delete-orphan')
    ship_favorites: Mapped[list['StarshipFavorites']] = relationship(back_populates='user', cascade='all, delete-orphan')

class Characters(db.Model):
    __tablename__= 'characters'
    char_id: Mapped[int] = mapped_column(primary_key = True)
    char_name: Mapped[int] = mapped_column(String, nullable = False, unique = True)
    gender: Mapped[str] = mapped_column(String, nullable = False)
    race: Mapped[str] = mapped_column(String, nullable = False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    allegiance: Mapped[str] = mapped_column(String, nullable = False)
    favorite_by: Mapped[list['CharacterFavorites']] = relationship(back_populates='character', cascade='all, delete-orphan')

class Planets(db.Model):
    __tablename__= 'planets'
    pla_id:Mapped[int] = mapped_column(primary_key = True)
    pla_name: Mapped[str] = mapped_column(String, nullable= False, unique = True)
    system: Mapped[str] = mapped_column(String, nullable= False,)
    Moons: Mapped[int] = mapped_column(Integer, nullable = False)
    favorite_by: Mapped[list['PlanetFavorites']] = relationship(back_populates='planet', cascade='all, delete-orphan')

class Starships(db.Model):
    __tablename__= 'starships'
    ship_id:Mapped[int] = mapped_column(primary_key = True)
    ship_name:Mapped[str] = mapped_column(String, nullable= False, unique = True)
    designer:Mapped[str] = mapped_column(String, nullable= False)
    affiliation: Mapped[str] = mapped_column(String, nullable = False)
    year_introduced:Mapped[int] = mapped_column(Integer, nullable = False)
    favorite_by: Mapped[list['StarshipFavorites']] = relationship(back_populates='starship', cascade='all, delete-orphan')    


class CharacterFavorites(db.Model):
    __tablename__ = 'character_favorites'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='char_favorites')
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.char_id'))
    character: Mapped['Characters'] = relationship(back_populates='favorite_by')

class PlanetFavorites(db.Model):
    __tablename__ = 'planet_favorites'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='pla_favorites')
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.pla_id'))
    planet: Mapped['Planets'] = relationship(back_populates='favorite_by')

class StarshipFavorites(db.Model):
    __tablename__ = 'starship_favorites'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='ship_favorites')
    starship_id: Mapped[int] = mapped_column(ForeignKey('starships.ship_id'))
    starship: Mapped['Starships'] = relationship(back_populates='favorite_by')            