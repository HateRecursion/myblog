from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post,Category,Tag

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-created_time')[:4]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['loop_counter']=range(1,5)
        return context


class AchiveView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.filter(created_time__year=self.kwargs.get('year'),
                                   created_time__month=self.kwargs.get('month'))


class ArticleView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(ArticleView, self).get(request, *args, **kwargs)
        self.object.increase_view()
        return response


class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(category=cate)


class TagView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return Post.objects.filter(tags=tag)


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')