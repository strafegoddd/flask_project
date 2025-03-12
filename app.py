from flask import Flask, render_template, request
from db import db
from models import Film, Genre, Language, Actor, Cast
from sqlalchemy import func

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/database', methods=['GET'])
    def show_database():
        selected_table = request.args.get('table', 'films') 

        data = {
            "films": Film.query.all(),
            "genres": Genre.query.all(),
            "languages": Language.query.all(),
            "actors": Actor.query.all(),
            "cast": Cast.query.all()
        }

        return render_template("database.twig", tables=data.keys(), selected_table=selected_table, data=data[selected_table])

    @app.route('/queries')
    def queries():
        query_option = request.args.get("query", "genre_counts")

        queries_dict = {
            "genre_counts": ("Количество фильмов в каждом жанре", 
                db.session.query(Genre.genre_name, func.count(Film.film_id))
                .join(Film)
                .group_by(Genre.genre_name)
                .all()),

            "avg_rating_by_language": ("Средний рейтинг фильмов по языку", 
                db.session.query(Language.language_name, func.avg(Film.film_rating))
                .join(Film)
                .group_by(Language.language_name)
                .all()),

            "most_expensive_film": ("Самый дорогой фильм в каждом жанре", 
                db.session.query(Genre.genre_name, Film.film_name, func.max(Film.film_budget))
                .join(Film)
                .group_by(Genre.genre_name)
                .all()),

            "actors_per_film": ("Количество актеров в каждом фильме", 
                db.session.query(Film.film_name, func.count(Cast.actor_id))
                .join(Cast)
                .group_by(Film.film_name)
                .all()),

            "avg_budget_by_genre": ("Средний бюджет фильмов по жанру", 
                db.session.query(Genre.genre_name, func.avg(Film.film_budget))
                .join(Film)
                .group_by(Genre.genre_name)
                .all())
        }

        title, result = queries_dict.get(query_option, queries_dict["genre_counts"])

        return render_template("queries.twig", title=title, result=result, selected_query=query_option)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
