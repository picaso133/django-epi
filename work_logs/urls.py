from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='order_index'),
    url(r'^new$', views.create, name='order_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='order_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='order_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='order_delete'),
]