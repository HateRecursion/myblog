from django.shortcuts import render,get_object_or_404,redirect
from .forms import CommentForm
from .models import Comment
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comments = post.comment_set.all()
            context = {
                'post':post,
                'comment_list':comments,
                'form':form,
            }
            return render(request, 'blog/single.html', context=context)
    else:
        redirect(post)