from django.shortcuts import render
from .models import Project
from .models import Curssos
from .models import Inscripcions

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html",
                  {'projects':projects})
    
def curssos(request):
    projects = Project.objects.all()
    return render(request, "portfolio/curssos.html",
                  {'projects':projects})


def inscripcions(request):
    projects = Project.objects.all()
    return render(request, "portfolio/inscripcions.html",
                  {'projects':projects})
