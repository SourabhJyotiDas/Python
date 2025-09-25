

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all-users/', views.all_users, name="All Users"),
]

