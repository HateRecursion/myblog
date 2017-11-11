from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        Post.objects.order_by('-created_time')[0:6]