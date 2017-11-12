from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='article'),
    url(r'^contact/$', views.contact,name='contact'),
    url(r'^about/$', views.about, name='about'),
]
