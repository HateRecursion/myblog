from django.shortcuts import render,get_object_or_404,redirect
from .forms import CommentForm
from .models import Comment
from blog.models import Post
# Create your views here.
def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comments = post.comment_set.all()
            context = {
                'post':post,
                'comments':comments,
                'form':form,
            }
            return render(request, 'blog/single.html', context=context)
    else:
        redirect(post)