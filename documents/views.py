import datetime
from operator import itemgetter

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .models import Document, Document_type
from projects.models import Project
from employees.models import Employ

document_types = Document_type.objects.filter()
document_statuses = [
    'Approved', 'Cleared', 'Draft', 'In Process',
    'Paid', 'Pending Cancellation', 'Pending Review', 'Rejected',
    'Submitting', 'Unpaid'
]

def index(request, template_name='documents/index.html'):
    # Document_type(name='Quotes').save()
    # Document_type(name='Orders').save()
    # Document_type(name='Delivery Dockets').save()
    # Document_type(name='Sales and Purchase Invoices').save()
    # Document_type(name='Credit and Debit Notes').save()
    # Document_type(name='Payment/Remittance Advices').save()
    # Document_type(name='Checks').save()
    # Document_type(name='Receipts').save()
    # Document_type(name='Deposit Slip').save()
    # Document_type(name='Other').save()
    # Document_type(name='Change Order').save()

    list = Document.objects.all()
    data = {
        'list': list,
    }
    return render(request, template_name, data)

def create(request, template_name='documents/create.html'):

    data = {
        'document_types': document_types,
        'document_statuses': document_statuses,
    }
    if request.method == 'POST':
        new = Document()
        new.number = request.POST.get('number')
        new.date = request.POST.get('date', '1970-01-01 00:00:00')
        new.due_date = request.POST.get('due_date', '1970-01-01 00:00:00')
        new.payee = request.POST.get('payee')
        new.payer = request.POST.get('payer')
        new.description = request.POST.get('description')
        new.status = request.POST.get('status')
        new.amount = float(request.POST.get('amount'))
        new.type = Document_type.objects.get(pk=request.POST.get('type'))
        new.save()

        return redirect('document_read', new.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='documents/read.html'):
    item = get_object_or_404(Document, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='documents/create.html'):
    update = get_object_or_404(Document, pk=pk)
    data = {
        'document_types': document_types,
        'document_statuses': document_statuses,
        'item': update,
    }
    if request.method == 'POST':
        update.number = request.POST.get('number')
        update.date = request.POST.get('date', '1970-01-01 00:00:00')
        update.due_date = request.POST.get('due_date', '1970-01-01 00:00:00')
        update.payee = request.POST.get('payee')
        update.payer = request.POST.get('payer')
        update.description = request.POST.get('description')
        update.status = request.POST.get('status')
        update.amount = float(request.POST.get('amount'))

        update.type = Document_type.objects.get(pk=request.POST.get('type'))
        update.save()

        return redirect('document_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='timesheets/delete.html'):
    o = get_object_or_404(Document, pk=pk)
    o.delete()
    return redirect('document_index')
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deassign(request, project, id, template_name = 'file_storage/upload.html'):
    o = get_object_or_404(Project, pk=project)
    o.documents.remove(Document.objects.get(pk=id))
    o.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))