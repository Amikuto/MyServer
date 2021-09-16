from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("World!")


def about(request):
    return HttpResponse("<h2>Add some info1</h2>")


def contacts(request):
    return HttpResponse("<h3>Contact page</h3>")
