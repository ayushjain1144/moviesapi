from django.urls import include, path

urlpatterns = [
    path('', include('moviesapi.urls')),
    #path('admin/', admin.site.urls),
]