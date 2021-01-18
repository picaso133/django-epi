from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='document_index'),
    url(r'^new$', views.create, name='document_create'),
    url(r'^(?P<pk>\d+)$', views.read, name='document_read'),
    url(r'^edit/(?P<pk>\d+)$', views.update, name='document_update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='document_delete'),
    path('deassign/<str:project>/<int:id>', views.deassign, name="document_deassign")
]