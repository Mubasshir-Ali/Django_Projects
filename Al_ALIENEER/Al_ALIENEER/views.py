# views.py file is created Manually
# import django libraryes
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


