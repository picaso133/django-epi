from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Receipt
from projects.models import Project
from documents.models import Document, Document_type
from documents.views import document_types, document_statuses
from suppliers.models import Supplier
from customers.models import Customer

def index(request, template_name='receipts/index.html'):
    list = Receipt.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='receipts/create.html'):
    r_from = Supplier.objects.filter().order_by('name')
    r_to = Customer.objects.filter().order_by('name')
    document_type = Document_type.objects.get(uuid='1261abd933ef45f98f5ac149b2a14c62')
    document_status = 'Approved'
    data = {
        'r_from': r_from,
        'r_to': r_to,
        'document_type': document_type,
        'document_statuses': document_statuses,
        'document_status': document_status,
    }
    if request.method == 'POST':

        d = Document()
        d.number = document_type.start + 1
        d.date = request.POST.get('date')
        d.description = request.POST.get('description')
        d.status = request.POST.get('status')
        d.type = document_type
        d.amount = request.POST.get('amount')
        d.save()

        document_type.start += 1
        document_type.save()

        new = Receipt()
        new.r_from = Supplier.objects.get(pk=request.POST.get('r_from'))
        new.r_to = Customer.objects.get(pk=request.POST.get('r_to'))
        new.document = d
        new.save()
        return redirect('receipt_read', pk=new.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='receipts/read.html'):
    item = get_object_or_404(Receipt, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='receipts/create.html'):
    update = get_object_or_404(Receipt, pk=pk)
    r_from = Supplier.objects.filter().order_by('name')
    r_to = Customer.objects.filter().order_by('name')
    document_type = Document_type.objects.get(uuid='1261abd933ef45f98f5ac149b2a14c62')
    document_status = 'Approved'
    data = {
        'r_from': r_from,
        'r_to': r_to,
        'document_type': document_type,
        'document_statuses': document_statuses,
        'document_status': document_status,
        'item': update,
    }
    if request.method == 'POST':

        d = Document()
        d.number = document_type.start + 1
        d.date = request.POST.get('date')
        d.description = request.POST.get('description')
        d.status = request.POST.get('status')
        d.type = document_type
        d.amount = request.POST.get('amount')
        d.save()

        document_type.start += 1
        document_type.save()

        update.r_from = Supplier.objects.get(pk=request.POST.get('r_from'))
        update.r_to = Customer.objects.get(pk=request.POST.get('r_to'))
        update.document = d
        update.save()
        # return redirect('receipt_read', pk=update.id)
        return redirect('receipt_index')
    else:
        return render(request, template_name, data)

def delete(request, pk, template_name='receipts/delete.html'):
    o = get_object_or_404(Receipt, pk=pk)
    o.delete()
    return redirect('receipt_index')