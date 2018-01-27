from django.views import generic

from .models import movie

class MovieListView(generic.ListView):
    template_name = 'moviesapi/movie_list.html'

    def get_queryset(self):
        return movie.objects.all()

