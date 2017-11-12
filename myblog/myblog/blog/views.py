from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
class IndexView(ListView):
    queryset = Post.objects.order_by('-created_time')[:4]
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['loop_counter']=range(1,5)
        return context

class DetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'


def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')