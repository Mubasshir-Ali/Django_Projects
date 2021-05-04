"""Al_ALIENEER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="AIHome"),
    path("about/", views.about, name="About"),
    path("courses/", views.courses, name="Courses"),
    path("blog/", views.blog, name="Blog"),
    path("contact/", views.contact, name="Contact"),
    path("login/", views.login, name="Login"),
    path("signup/", views.signup, name="Sign"),
    path("forgot_password/", views.forgot_password, name="Forgot Password"),
    path("single_post/", views.single_post, name="Single Post"),
    # Dashboard urls
    path("dashboard/", views.dashboard, name="Dashboard"),
    # path("", views.index, name="AIHome"),
    # path("", views.index, name="AIHome"),
    # path("", views.index, name="AIHome"),
    # path("", views.index, name="AIHome"),
    # path("", views.index, name="AIHome"),
    

]
