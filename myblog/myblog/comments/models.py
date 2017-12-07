from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User,default="")
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-created_time']
