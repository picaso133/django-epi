from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='change_order_index'),
    url(r'^new$', views.create, name='change_order_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='change_order_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='change_order_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='change_order_delete'),
]