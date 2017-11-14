from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='article'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archivesView.as_view(), name='archives'),
    url(r'^contact/$', views.contact,name='contact'),
    url(r'^about/$', views.about, name='about'),
]
