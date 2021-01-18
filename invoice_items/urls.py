from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='invoice_item_index'),
    url(r'^new$', views.create, name='invoice_item_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='invoice_item_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='invoice_item_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='invoice_item_delete'),
]