from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='receipt_index'),
    url(r'^new$', views.create, name='receipt_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='receipt_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='receipt_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='receipt_delete'),
]