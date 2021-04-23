from django.shortcuts import render, redirect
from . models import *

def index(request):
    context = {
        "all_shows": Show.objects.all()
        }
    return render(request, "index.html", context) 

def create_show(request):
    Show.objects.create(title = request.POST['title'],network = request.POST['network'],release_date = request.POST['release_date'],description = request.POST['description'])
    return redirect("/")

def show(request, show_id):
    context={"this_show":Show.objects.get(id=show_id)}
    
    return render(request, "show.html", context)

def edit_show(request, show_id):
    context={"this_show":Show.objects.get(id=show_id)}
    return redirect(f"/edit.html/{show_id}", context)

def new_show(request):
    return render(request, "new_show.html")

def update_show(request, show_id):
    return redirect(f"/show/{show_id}")

def display_show(request, show_id):
    context={"show":Show.objects.get(id=show_id)}
    return render(request, "show.html", context)








