from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from change_orders.models import Change_order
from .models import Invoice
from invoice_items.models import Invoice_item
from projects.models import Project
from documents.models import Document, Document_type
from documents.views import document_types, document_statuses
from customers.models import Customer

change_order_statuses = ['Open', 'Sent', 'Under Review', 'Approved', 'Rejected', 'Canceled']

def index(request, template_name='invoices/index.html'):
    list = Invoice.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='invoices/create.html'):
    items = []
    customers = Customer.objects.filter()
    document_type = Document_type.objects.get(uuid='5b34bfb8f43e436aa57e044b3c5e1824')
    data = {
        'customers': customers,
        'document_type': document_type,
        'document_statuses': document_statuses,
        'document_status': 'Draft',
    }
    if request.method == 'POST':
        pass
        # return redirect('invoice_read', pk=i.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='invoices/read.html'):
    item = get_object_or_404(Invoice, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='invoices/create.html'):
    update = get_object_or_404(Invoice, pk=pk)
    items = []
    customers = Customer.objects.filter()
    document_type = Document_type.objects.get(uuid='5b34bfb8f43e436aa57e044b3c5e1824')
    data = {
        'customers': customers,
        'document_type': document_type,
        'document_statuses': document_statuses,
        'document_status': 'Draft',
        'item': update
    }
    if request.method == 'POST':
        pass
        # return redirect('change_order_read', pk=new.id)
    else:
        return render(request, template_name, data)

def delete(request, pk):
    get_object_or_404(Invoice_item, pk=pk).delete()
    return HttpResponse(request.META.get('HTTP_REFERER'))