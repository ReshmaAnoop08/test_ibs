from django.shortcuts import render
from movieapp.tasks import Movie_view
from movieapp.models import Movie
from datetime import datetime
from django.http import JsonResponse


# Create your views here.
def movie_list(request):
    movie_obj=Movie.objects.all()
    return render(request, 'movieapp/movie_list.html', {'movie_obj':movie_obj})

def add_movie(request):
    if request.method == "POST":
        movie_name = request.POST.get('mname')
        movie_genre = request.POST.get('mgenre')
        movie_studio = request.POST.get('mstudio')
        movie_director = request.POST.get('mdirector')
        movie_cast = request.POST.get('mcast')
        movie_box = request.POST.get('mbox')
        movie_release = request.POST.get('mrelease')
        movie_obj = Movie.objects.create(movie_name = movie_name, movie_genre = movie_genre,
        movie_studio = movie_studio, movie_director = movie_director, Movie_cast = movie_cast,
         box_office_collection = movie_box, release_date = movie_release)
        # Movie_view.delay(movie_name, movie_genre, movie_studio, movie_director, movie_cast, movie_box, movie_release)
        movie_obj=Movie.objects.all()
        return render(request, 'movieapp/movie_list.html', {'movie_obj':movie_obj})
    else:
        return render(request, 'movieapp/add_movie.html', {})

def edit_movie(request,pk):
    if request.method == "POST":
        movie_name = request.POST.get('mname')
        movie_genre = request.POST.get('mgenre')
        movie_studio = request.POST.get('mstudio')
        movie_director = request.POST.get('mdirector')
        movie_cast = request.POST.get('mcast')
        movie_box = request.POST.get('mbox')
        movie_release = request.POST.get('mrelease')
        movie_obj = Movie.objects.get(pk=pk)
        movie_obj.movie_name = movie_name
        movie_obj.movie_genre = movie_genre
        movie_obj.movie_studio = movie_studio
        movie_obj.movie_director = movie_director
        movie_obj.Movie_cast = movie_cast
        movie_obj.box_office_collection = movie_box
        movie_obj.release_date = movie_release
        movie_obj.save()
        movie_obj=Movie.objects.all()
        return render(request, 'movieapp/movie_list.html', {'movie_obj':movie_obj})
    else:
        movie_obj = Movie.objects.get(pk=pk)
        date_object = movie_obj.release_date.strftime('%Y-%m-%d')
        return render(request, 'movieapp/edit_movie.html', {'movie_obj':movie_obj,'date_object':date_object})

def delete_movie(request,pk):
    movie_obj = Movie.objects.get(pk=pk)
    movie_obj.delete()
    movie_obj=Movie.objects.all()
    return render(request, 'movieapp/movie_list.html', {'movie_obj':movie_obj})

def add_rating(request):
    print(request.method)
    if request.method == "POST":
        movie_name = request.POST.get('mname')
        movie_genre = request.POST.get('mgenre')
        movie_studio = request.POST.get('mstudio')
        movie_director = request.POST.get('mdirector')
        movie_cast = request.POST.get('mcast')
        movie_box = request.POST.get('mbox')
        movie_release = request.POST.get('mrelease')
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        movie_obj = Movie.objects.get(id=el_id)
        movie_obj.movie_name = movie_name
        movie_obj.movie_genre = movie_genre
        movie_obj.movie_studio = movie_studio
        movie_obj.movie_director = movie_director
        movie_obj.Movie_cast = movie_cast
        movie_obj.box_office_collection = movie_box
        movie_obj.release_date = movie_release
        movie_obj.rating = val
        movie_obj.save()
        movie_obj=Movie.objects.all()
        return render(request, 'movieapp/movie_list.html', {'movie_obj':movie_obj})
    else:
        print("jjjjj")
        movie_obj = Movie.objects.get(pk=6)
        date_object = movie_obj.release_date.strftime('%Y-%m-%d')
        return render(request, 'movieapp/add_rating.html', {'movie_obj':movie_obj,'date_object':date_object})
