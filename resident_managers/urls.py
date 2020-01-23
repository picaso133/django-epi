from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='resident_manager_index'),
    url(r'^new$', views.create, name='resident_manager_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='resident_manager_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='resident_manager_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='resident_manager_delete'),
]