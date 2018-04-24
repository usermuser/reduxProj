# from django.shortcuts import render
from django.http import HttpResponse


def landing_view(request):
    return HttpResponse("Hello, world. This is a landing page.")
