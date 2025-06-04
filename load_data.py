# import pandas as pd
# from datetime import datetime
# from app import db, app
# from models import Genre, Language, Film, Actor, Cast

# def process_budget(value):
#     """Конвертирует строковый бюджет в число"""
#     try:
#         return int(float(value.replace('$', '').replace('M', '')) * 1_000_000)
#     except:
#         return None

# def load_data():
#     df = pd.read_csv('data/cleaned_movies.csv')

#     with app.app_context():
#         for _, row in df.iterrows():
#             # Обрабатываем жанры
#             genre_name = eval(row['Genres'])[0]  # Берём первый жанр
#             genre = Genre.query.filter_by(genre_name=genre_name).first()
#             if not genre:
#                 genre = Genre(genre_name=genre_name)
#                 db.session.add(genre)
#                 db.session.flush()  # Получаем genre_id

#             # Обрабатываем язык (первый в списке)
#             language_name = eval(row['Original_Language'])[0]
#             language = Language.query.filter_by(language_name=language_name).first()
#             if not language:
#                 language = Language(language_name=language_name)
#                 db.session.add(language)
#                 db.session.flush()  # Получаем language_id

#             # Добавляем фильм
#             film = Film(
#                 film_name=row['Movie_Name'],
#                 film_date=None,  # Даты нет в CSV, можно позже добавить
#                 film_rating=row['Vote_Average'],
#                 film_budget=process_budget(row['Budget_USD']),
#                 genre_id=genre.genre_id,
#                 language_id=language.language_id
#             )
#             db.session.add(film)
#             db.session.flush()  # Получаем film_id

#             # Обрабатываем актёров и связи с фильмами
#             actors = eval(row['Cast'])
#             for actor_name in actors:
#                 actor = Actor.query.filter_by(actor_name=actor_name).first()
#                 if not actor:
#                     actor = Actor(actor_name=actor_name)
#                     db.session.add(actor)
#                     db.session.flush()

#                 # Добавляем связь Cast
#                 cast_entry = Cast(film_id=film.film_id, actor_id=actor.actor_id)
#                 db.session.add(cast_entry)

#         db.session.commit()

# if __name__ == '__main__':
#     load_data()
#     print("Данные загружены успешно!")
