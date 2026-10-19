from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student


def home(request):
    return HttpResponse("Love project works!")


def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', locals())