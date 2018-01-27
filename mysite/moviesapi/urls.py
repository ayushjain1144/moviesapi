from django.conf.urls import url
from . import views

app_name = 'moviesapi'

urlpatterns = [
    url('', views.MovieListView.as_view(), name = 'movie_list'),
    #path('admin/', admin.site.urls),
]