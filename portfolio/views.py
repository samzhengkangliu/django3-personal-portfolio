from django.shortcuts import render
from .models import Project


def home(request):
    # grab all the Project objects from db
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
