from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"message": "Hello World Django App"}
    return render(request, "myapp/index.html", context)
