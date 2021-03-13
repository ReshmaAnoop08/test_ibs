from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length = 400)
    movie_genre = models.TextField()
    movie_studio = models.TextField()
    movie_director = models.TextField()
    Movie_cast = models.TextField()
    box_office_collection = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)
    rating = models.IntegerField(default=0,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0),

            ]

    )

    def __str__(self):
        return self.movie_name
