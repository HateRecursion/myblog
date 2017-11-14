from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count

#模板标签可以返回任意的python数据结构，在模板中解析出来即可
register = template.Library()

@register.simple_tag
def get_recent_post_list(num=5):
    return Post.objects.order_by("-created_time")[:num]

@register.simple_tag
def get_most_viewd_posts(num=5):
    return Post.objects.order_by("view")[:num]

#先按月份的粒度，把时间倒序提取出来，再根据特定的月份查找数量，构造元组的列表后返回解析
@register.simple_tag
def get_post_date_monthly():
    post_dates = Post.objects.dates('created_time', 'month', order='DESC')
    post_data=[]
    for post in post_dates:
        num = Post.objects.filter(created_time__year=post.year, created_time__month=post.month).count()
        print("year %d, month %d, num:%d" % (post.year, post.month, num))
        post_data.append((post.year,post.month,num))
    return post_data

@register.simple_tag
def get_categories():
    return Category.objects.annotate(post_num=Count('post')).filter(post_num__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(post_num=Count('post')).filter(post_num__gt=0)
