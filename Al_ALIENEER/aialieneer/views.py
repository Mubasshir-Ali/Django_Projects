from django.shortcuts import render
from django.http import HttpResponse
# from .models import Course
from django.db.models import Count
from .models import *
from math import ceil

# Create your views here.
def index(request):
    # courses = Course.objects.order_by('id')
    # courses = Course.objects.all()[:6]
    courses = Course.objects.order_by('pub_date')[0:6]
    # posts = Post.updateMany( {}, { $rename: { "post_type": "text" } } )
    # courses = Course.objects.last()
    # print(courses)
    # n = len(courses)
    # ncols = n//4 + ceil((n/4) - (n//4))
    # params = {'no_of_columns': ncols, 'range':range(1,ncols), 'course':courses}
    machnelearning = Course.objects.filter(course_category='ML')
    dl = Course.objects.filter(course_category='DL')
    cv = Course.objects.filter(course_category='CV')
    nlp = Course.objects.filter(course_category='NLP')
    return render(request, 'aialieneer/index.html',{'courses': courses, 'machnelearning':machnelearning, 'dl':dl})

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