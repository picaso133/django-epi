"""django_epi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('receipts/', include('receipts.urls')),
    path('invoices/', include('invoices.urls')),
    path('invoice_items/', include('invoice_items.urls')),
    path('documents/', include('documents.urls')),
    path('work_logs/', include('work_logs.urls')),
    path('timesheets/', include('timesheets.urls')),
    path('inventory/', include('inventory.urls')),
    path('orders/', include('orders.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('change_orders/', include('change_orders.urls')),
    path('project_managers/', include('project_managers.urls')),
    path('resident_managers/', include('resident_managers.urls')),
    path('permits/', include('permits.urls')),
    path('inspection_types/', include('inspection_types.urls')),
    path('inspections/', include('inspections.urls')),
    path('projects/', include('projects.urls')),
    path('checks/', include('checks.urls')),
    path('employees/', include('employees.urls')),
    path('file_storage/', include('file_storage.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
