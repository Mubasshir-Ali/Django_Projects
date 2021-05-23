from django.contrib import admin

# Register your models here.
# from .models import Course, Post, Single_Post
from .models import *

admin.site.register(Course)
admin.site.register(Post)
# admin.site.register(Single_Post)