
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name="homepage"),
    path('author/', include('Author.urls')),
    path('posts/', include('Posts.urls')),
    path('profiles/', include('Profiles.urls')),
    path('cetagories/', include('Cetagories.urls')),
]
