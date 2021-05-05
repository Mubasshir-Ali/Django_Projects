from django.db import models

# Create your models here.

class Course(models.Model):
    _id = models.AutoField
    course_name = models.CharField(max_length=100)
    course_author = models.CharField(max_length=100)
    pub_date = models.DateField()
    course_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "aialieneer/images", default = "")

    def __str__(self):
        return self.course_name
