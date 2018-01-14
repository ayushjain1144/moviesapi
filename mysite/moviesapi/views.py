from django.views import generic

from moviesapi.models import movie

class MovieListView(generic.ListView):
    model = movie

