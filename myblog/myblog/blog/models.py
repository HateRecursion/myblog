from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tags(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt=models.CharField(max_length=200, blank=True)
    view = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category)
    tags=models.ManyToManyField(Tags)
    author = models.ForeignKey(User)