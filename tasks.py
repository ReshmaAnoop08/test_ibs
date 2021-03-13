from moviesite.celery import app
from movieapp.models import Movie
@app.task
def Movie_view(movie_name,movie_genre,movie_studio,movie_director, Movie_cast, box_office_collection, release_date, rating=None):
   try:
       movie_obj = Movie.objects.create(movie_name = movie_name, movie_genre = movie_genre,
       movie_studio = movie_studio, movie_director = movie_director, Movie_cast = Movie_cast,
        box_office_collection = box_office_collection, release_date = release_date, rating=rating)
       return {"status": True}
   except Exception:
       return {"status": False}
