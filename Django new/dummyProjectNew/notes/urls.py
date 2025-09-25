
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all-notes/', views.all_notes, name="All Notes"),
]
