from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.utils.html import strip_tags

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

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
    tags=models.ManyToManyField(Tag)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse("blog:article", kwargs={'pk':self.pk})

    def increase_view(self):
        self.view+=1
        self.save(update_fields=['view'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:54]
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']