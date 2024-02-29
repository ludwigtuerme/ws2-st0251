from django.core.management.base import BaseCommand
from movie.models import Movie

import os
import json

class Command(BaseCommand):
  help = "Load movies from movies.json into the Movie model."

  def handle(self, *args, **kwargs):
    json_file_path = "movie/management/commands/movies.json"

    with open(json_file_path, "r") as file:
      movies = json.load(file)

    for i in range(99):  # I think I actually have 99 movies. Oops.
      movie = movies[i]
      exists = Movie.objects.filter(title=movie["title"]).first()
      if not exists:
        Movie.objects.create(
          title=movie["title"],
          image="movie/images/default.png",
          genre=movie["genre"],
          year=movie["year"],)
