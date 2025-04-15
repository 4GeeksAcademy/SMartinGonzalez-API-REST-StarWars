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
    char_favorites: Mapped[list['CharacterFavorites']] = relationship(back_populates='user', cascade='all, delete-orphan', lazy= 'joined')
    pla_favorites: Mapped[list['PlanetFavorites']] = relationship(back_populates='user', cascade='all, delete-orphan', lazy= 'joined')
    ship_favorites: Mapped[list['StarshipFavorites']] = relationship(back_populates='user', cascade='all, delete-orphan', lazy= 'joined')

    def __repr__(self):
       return f'Usuario con id {self.id} y nombre {self.name}' 


    def serialize(self):
     return {
        'user_id': self.id,
        'username': self.name,
        'lastname': self.lastname,
        'email': self.email,
        'password': self.password,
        'is_active': self.is_active
    }


class Characters(db.Model):
    __tablename__= 'characters'
    char_id: Mapped[int] = mapped_column(primary_key = True)
    char_name: Mapped[int] = mapped_column(String, nullable = False, unique = True)
    gender: Mapped[str] = mapped_column(String, nullable = False)
    race: Mapped[str] = mapped_column(String, nullable = False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    allegiance: Mapped[str] = mapped_column(String, nullable = False)
    favorite_by: Mapped[list['CharacterFavorites']] = relationship(back_populates='character', cascade='all, delete-orphan', lazy= 'joined')

    def __repr__(self):
       return f'Personaje con id {self.char_id} y nombre {self.char_name}' 

    def serialize(self):
     return {
        'char_id': self.char_id,
        'char_name': self.char_name,
        'gender': self.gender,
        'race': self.race,
        'height': self.height,
        'allegiance': self.allegiance
    }

class Planets(db.Model):
    __tablename__= 'planets'
    pla_id:Mapped[int] = mapped_column(primary_key = True)
    pla_name: Mapped[str] = mapped_column(String, nullable= False, unique = True)
    system: Mapped[str] = mapped_column(String, nullable= False,)
    moons: Mapped[int] = mapped_column(Integer, nullable = False)
    favorite_by: Mapped[list['PlanetFavorites']] = relationship(back_populates='planet', cascade='all, delete-orphan', lazy= 'joined')

    def __repr__(self):
       return f'Planeta con id {self.pla_id} y nombre {self.pla_name}' 
    
    def serialize(self):
     return {
        'pla_id': self.pla_id,
        'pla_name': self.pla_name,
        'system': self.system,
        'moons': self.moons
    }


class Starships(db.Model):
    __tablename__= 'starships'
    ship_id:Mapped[int] = mapped_column(primary_key = True)
    ship_name:Mapped[str] = mapped_column(String, nullable= False, unique = True)
    designer:Mapped[str] = mapped_column(String, nullable= False)
    affiliation: Mapped[str] = mapped_column(String, nullable = False)
    year_introduced:Mapped[int] = mapped_column(Integer, nullable = False)
    favorite_by: Mapped[list['StarshipFavorites']] = relationship(back_populates='starship', cascade='all, delete-orphan', lazy= 'joined')


    def __repr__(self):
       return f'Starship con id {self.ship_id} y nombre {self.ship_name}' 

    def serialize(self):
     return {
        'ship_id': self.ship_id,
        'ship_name': self.ship_name,
        'designer': self.designer,
        'affiliation': self.affiliation,
        'year_introduced': self.year_introduced
    }    


class CharacterFavorites(db.Model):
    __tablename__ = 'character_favorites'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='char_favorites')
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.char_id'))
    character: Mapped['Characters'] = relationship(back_populates='favorite_by')

    def __repr__(self):
     return f'Al usuario {self.user_id} le gusta el personaje {self.character_id}' 

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