from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='project_index'),
    path('done', views.index_inactive, name='project_done'),
    path('api_get', views.api_get, name='project_api_get'),
    url(r'^$', views.index, name='project_index'),
    url(r'^new$', views.create, name='project_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='project_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='project_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='project_delete'),
]