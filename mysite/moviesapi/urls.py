from django.urls import path
from . import views

app_name = 'moviesapi'

urlpatterns = [
    path('movie/', views.MovieListView.as_view(), name='movie'),
    path('movie/<int:pk>', views.MovieListView.as_view(), name='movie-detail'),
]