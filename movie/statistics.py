import base64
import io
import urllib
from collections import defaultdict

import matplotlib
import matplotlib.pyplot as plt

from .models import Movie


def generate_movies_per_year_chart():
  matplotlib.use("Agg")
  years = Movie.objects.values_list("year", flat=True).distinct().order_by("year")
  movie_counts_by_year = {}
  for year in years:
    if year:
      movies_in_year = Movie.objects.filter(year=year)
    else:
      movies_in_year = Movie.objects.filter(year__isnull=True)
      year = "None"
    movie_counts_by_year[year] = movies_in_year.count()

  bar_width = 0.5
  bar_spacing = 0.5
  bar_positions = range(len(movie_counts_by_year))

  plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width)
  plt.title("Movies per year")
  plt.xlabel("Year")
  plt.ylabel("Number of movies")
  plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)

  plt.subplots_adjust(bottom=0.3)

  buffer = io.BytesIO()
  plt.savefig(buffer, format="png")
  buffer.seek(0)
  plt.close()

  image_png = buffer.getvalue()
  buffer.close()
  years_chart = base64.b64encode(image_png)
  years_chart = years_chart.decode("utf-8")

  return years_chart

def generate_movies_per_genre_chart():
  genres = Movie.objects.values_list("genre", flat=True)

  genre_counts = defaultdict(int)
  for entry in genres:
    first_genre = entry.split(",")[0]
    if first_genre is not "":
      genre_counts[first_genre] += 1
    else:
      genre_counts["None"] += 1

  matplotlib.use("Agg")

  bar_width = 0.5
  bar_spacing = 0.5
  bar_positions = range(len(genre_counts))

  plt.bar(bar_positions, genre_counts.values(), width=bar_width)
  plt.title("Movies per genre")
  plt.xlabel("Genre")
  plt.ylabel("Number of movies")
  plt.xticks(bar_positions, genre_counts.keys(), rotation=90)

  plt.subplots_adjust(bottom=0.3)

  buffer = io.BytesIO()
  plt.savefig(buffer, format="png")
  buffer.seek(0)
  plt.close()

  image_png = buffer.getvalue()
  buffer.close()
  years_chart = base64.b64encode(image_png)
  years_chart = years_chart.decode("utf-8")

  return years_chart
