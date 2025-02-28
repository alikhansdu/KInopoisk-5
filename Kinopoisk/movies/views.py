from django.shortcuts import render, get_object_or_404, redirect


from django.shortcuts import render
from .models import Movie

def movie_list(request):
    genre = request.GET.get("genre", "")
    year = request.GET.get("year", "")

    movies = Movie.objects.all()

    if genre:
        movies = movies.filter(genre=genre)

    if year:
        movies = movies.filter(release_date__year=year)

    # Достаем уникальные жанры и года из базы
    genres = Movie.objects.values_list("genre", flat=True).distinct()
    years = Movie.objects.dates("release_date", "year", order="DESC")

    return render(request, "movie_list.html", {"movies": movies, "genres": genres, "years": years})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movie_list')
