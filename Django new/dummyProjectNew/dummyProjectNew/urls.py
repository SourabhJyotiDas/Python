
from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Hello Home"),
    path('about/', views.about, name="Hello About"),
    path('notes/', include("notes.urls")),
    path('users/', include("users.urls")),
]
