# Generated by Django 3.2.1 on 2021-05-10 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aialieneer', '0002_course_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-pub_date']},
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_name',
        ),
        migrations.AddField(
            model_name='course',
            name='course_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]