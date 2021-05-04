from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'aialieneer/index.html')

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

def dashboard(request):
    return render(request, 'aialieneer/dashboard.html')