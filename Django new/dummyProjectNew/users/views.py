from django.shortcuts import render

# Create your views here.


def all_users(req):
    return render(req, "users/all_users.html")
