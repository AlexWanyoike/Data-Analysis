from django.shortcuts import render, redirect

from .models import Student

# Create your views here.
def analysis(request):
    return render(request , './main.html')

