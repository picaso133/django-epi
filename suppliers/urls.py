from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='supplier_index'),
    url(r'^new$', views.create, name='supplier_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='supplier_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='supplier_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='supplier_delete'),
]