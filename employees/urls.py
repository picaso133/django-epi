from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='employ_index'),
    url(r'^new$', views.create, name='employ_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='employ_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='employ_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='employ_delete'),
]