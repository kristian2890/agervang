from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import vagt
from .utils import calendarMonth


# Create your views here. 
def index(request):
    return render(request, "vagtplan/index.html", {
        "cMonth": calendarMonth
    })

person = ['Ellen', 'Joachim', 'Sarah']
def greet(request, name):
    return render(request, "vagtplan/greet.html", {
        "name": name.capitalize(),
        "person": person
    })

