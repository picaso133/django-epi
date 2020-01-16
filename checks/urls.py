from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='check_index'),
    url(r'^new$', views.create, name='check_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='check_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='check_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='check_delete'),
]