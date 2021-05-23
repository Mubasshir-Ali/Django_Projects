# Generated by Django 3.2.3 on 2021-05-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aialieneer', '0005_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='', max_length=1000),
        ),
    ]