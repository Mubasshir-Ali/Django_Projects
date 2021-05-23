from django.db import models
# from djangotoolbox.fields import ListField
from mongoengine import *
import mongoengine
# import pymongo
import datetime

# Create your models here.
########################################################################
#                       MongoDb Collection Course
########################################################################

class Course(models.Model):
    _id = models.AutoField
    course_title = models.CharField(max_length=100)
    slug = models.SlugField()
    course_author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    course_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "aialieneer/images", default = "")

    def __str__(self):
        return self.course_title
    
    class Meta:
        ordering = ['-pub_date']

########################################################################
#                       MongoDb Collection Post
########################################################################

class Post(models.Model):
    _id = models.AutoField
    post_title = models.CharField(max_length=100)
    slug = models.SlugField()
    post_author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000, default = "")
    comments = models.TextField(max_length=1000, default = "")
    image = models.ImageField(upload_to = "aialieneer/images", default = "")

    def __str__(self):
        return self.post_title
    
    class Meta:
        ordering = ['-pub_date']

# django.db.Post.updateMany( {}, { $rename: { "nmae": "name" } } )


# class Post(models.Model):
#     title = models.CharField()
#     text = models.TextField()
#     tags = ListField()
#     comments = ListField()

########################################################################
#                       pymongo Database Setup
########################################################################

# client = pymongo.MongoClient(host="localhost", port=27017)

# db = client['aialieneer']

########################################################################
#                    Create Collections Means Tables
########################################################################
# col_posts = db['posts']

# posts_data = {'post_title':'AI', 'post_slug':'ai', 'post_author':'PAGAL', 'pub_date': datetime.datetime.now(), 'url':'aialieneer/images'}

# col_posts.insert_one(posts_data)

# course_data = {'course_title':'IS', 'course_slug':'is', 'course_author':'PAGAL', 'pub_date': datetime.datetime.now(), 'url':'aialieneer/images'}

# Course.insert_one(course_data)

#print(db.list_collection_names())

# from mongoengine import connect
# from mongoengine import Document, StringField, IntField
# # from models import User

# # Connect to MongoDB
# # connect(db="aialieneer", host="localhost", port=27017)

# from mongoengine import Document, fields

# class Single_Post(Document):
#     s_post_title = fields.StringField(max_length=100)
#     s_slug = fields.StringField(max_length=100)
#     s_post_author = fields.StringField(max_length=100)
#     s_pub_date = fields.DateField(default=...)
#     s_post_comment = fields.StringField(max_length=100)
#     s_post_desc = fields.StringField(max_length = 1000)
#     image = fields.ImageField(upload_to = "aialieneer/images", default = "")


