from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post,Category,Tag
from comments.forms import CommentForm
import markdown
# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        paginate_data = self.paginate_data(paginator, page ,is_paginated)
        context.update(paginate_data)
        return context

    def paginate_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_show_num = 1
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            #page_range[0]对应第1页，right[0]是当前页的下一页
            right = page_range[page_number : page_number+ page_show_num]
            if right[-1] < total_pages -1 :
                right_has_more=True
            if right[-1] < total_pages:
                last=True
        elif page_number == total_pages:
            left = page_range[(page_number - page_show_num - 1) if (page_number - page_show_num - 1) > 0 else 0 : page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - page_show_num - 1) if (page_number - page_show_num - 1) > 0 else 0 : page_number - 1]
            right = page_range[page_number : page_number+ page_show_num]
            if right[-1] < total_pages -1 :
                right_has_more=True
            if right[-1] < total_pages:
                last=True
            if left[0] > page_show_num:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }
        return data

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
        print(self.object.pk)
        return response

    def get_object(self, queryset=None):
        post = super(ArticleView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body, extensions = [
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
        return post

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context['form'] = form
        context['comment_list'] = comment_list
        return context



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