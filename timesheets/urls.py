from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='timesheet_index'),
    url(r'^new$', views.create, name='timesheet_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='timesheet_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='timesheet_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='timesheet_delete'),
]