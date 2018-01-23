from django.views import generic

from .models import movie

class MovieListView(generic.ListView):
    model = movie

