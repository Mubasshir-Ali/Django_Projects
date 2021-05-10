from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from math import ceil

# Create your views here.
def index(request):
    courses = Course.objects.all()
    # print(courses)
    # n = len(courses)
    # ncols = n//4 + ceil((n/4) - (n//4))
    # params = {'no_of_columns': ncols, 'range':range(1,ncols), 'course':courses}
    return render(request, 'aialieneer/index.html',{'courses': courses})

def about(request):
    return render(request, 'aialieneer/about.html')

def courses(request):
    return render(request, 'aialieneer/courses.html')

def blog(request):
    return render(request, 'aialieneer/blog.html')

def contact(request):
    return render(request, 'aialieneer/contact.html')

def login(request):
    return render(request, 'aialieneer/login.html')

def signup(request):
    return render(request, 'aialieneer/signup.html')

def forgot_password(request):
    return render(request, 'aialieneer/forgot-password.html')

def single_post(request):
    return render(request, 'aialieneer/single-post.html')

def single_courses(request):
    return render(request, 'aialieneer/single-courses.html')

def dashboard(request):
    return render(request, 'aialieneer/dashboard.html')