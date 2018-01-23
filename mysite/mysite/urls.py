from django.urls import include, path

urlpatterns = [
    path('polls/', include('moviesapi.urls')),
    path('admin/', admin.site.urls),
]