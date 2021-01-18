from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='work_log_index'),
    url(r'^new$', views.create, name='work_log_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='work_log_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='work_log_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='work_log_delete'),
]