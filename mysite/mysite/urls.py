from django.urls import path
from moviesapi.views import MovieListView

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/', views.MovieListView.as_view(), name='movie'),
    path('movie/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
]