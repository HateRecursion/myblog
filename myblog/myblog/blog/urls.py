from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleView.as_view(), name='article'),
    url(r'^article/add/$', views.add_article ,name='add_article'),
    url(r'^article/edit/(?P<pk>[0-9]+)/$', views.edit_article, name='edit_article'),
    url(r'^article/delete/(?P<pk>[0-9]+)/$', views.delete_article, name='delete_article'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.AchiveView.as_view(), name='archives'),
    url(r'^categoriy/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page':'/'}),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^contact/$', views.contact,name='contact'),
    url(r'^about/$', views.about, name='about'),
]
