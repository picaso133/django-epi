from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='permit_index'),
    url(r'^new$', views.create, name='permit_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='permit_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='permit_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='permit_delete'),
]