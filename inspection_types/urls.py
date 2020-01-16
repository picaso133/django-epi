from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='inspection_type_index'),
    url(r'^new$', views.create, name='inspection_type_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='inspection_type_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='inspection_type_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='inspection_type_delete'),
]