from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='inventory_index'),
    url(r'^new$', views.create, name='inventory_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='inventory_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='inventory_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='inventory_delete'),
]