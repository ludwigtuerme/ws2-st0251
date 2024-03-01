from django.shortcuts import render
from django.http import HttpResponse

from .statistics import generate_movies_per_genre_chart, generate_movies_per_year_chart
from .models import Movie

# Create your views here.

def home(request):
  searchTerm = request.GET.get("searchMovie")
  if searchTerm:
    movies = Movie.objects.filter(title__icontains=searchTerm)
  else:
    movies = Movie.objects.all()
  return render(request, "home.html", {"searchTerm": searchTerm, "movies": movies})

def about(request):
  return render(request, "about.html")

def signup(request):
  email = request.GET.get("email")
  return render(request, "signup.html", {"email": email})

def statistics_view(request):
  years_chart = generate_movies_per_year_chart()
  genres_chart = generate_movies_per_genre_chart()
  return render(request, "statistics.html",
                {"years_chart": years_chart, "genres_chart": genres_chart})
