from django.shortcuts import render

# Create your views here.

def all_notes (req):
    return render(req,"notes/all_notes.html")