from db import db

# Таблица Жанры
class Genre(db.Model):
    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(100), nullable=False, unique=True)

# Таблица Языки
class Language(db.Model):
    __tablename__ = 'languages'
    language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(100), nullable=False, unique=True)

# Таблица Фильмы
class Film(db.Model):
    __tablename__ = 'films'
    film_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_name = db.Column(db.String(255), nullable=False)
    film_date = db.Column(db.Date, nullable=True)
    film_rating = db.Column(db.Float)
    film_budget = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.language_id'), nullable=False)

    # Отношения
    genre = db.relationship('Genre', backref='films')
    language = db.relationship('Language', backref='films')
    actors = db.relationship('Actor', secondary='cast', backref='films')

# Таблица Актёры
class Actor(db.Model):
    __tablename__ = 'actors'
    actor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actor_name = db.Column(db.String(255), nullable=False, unique=True)

# Таблица-связь Cast
class Cast(db.Model):
    __tablename__ = 'cast'
    film_id = db.Column(db.Integer, db.ForeignKey('films.film_id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.actor_id'), primary_key=True)
