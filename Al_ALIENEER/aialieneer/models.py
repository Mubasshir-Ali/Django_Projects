from django.db import models

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

