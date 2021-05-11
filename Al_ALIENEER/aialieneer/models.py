from django.db import models
import pymongo
import datetime

# Create your models here.

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
#                       pymongo Database Setup
########################################################################

client = pymongo.MongoClient(host="localhost", port=27017)

db = client['aialieneer']

########################################################################
#                    Create Collections Means Tables
########################################################################
col_posts = db['posts']

posts_data = {'post_title':'AI', 'post_slug':'ai', 'post_author':'PAGAL', 'pub_date': datetime.datetime.now(), 'url':'aialieneer/images'}

col_posts.insert_one(posts_data)

#print(db.list_collection_names())