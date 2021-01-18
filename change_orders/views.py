from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Change_order
from projects.models import Project
from documents.models import Document, Document_type
from documents.views import document_types, document_statuses

change_order_statuses = ['Open', 'Sent', 'Under Review', 'Approved', 'Rejected', 'Canceled']

def index(request, template_name='change_orders/index.html'):
    list = Change_order.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='change_orders/create.html'):
    projects = Project.objects.filter()
    document_type = Document_type.objects.get(uuid='983112f663c54640988dd7222299f3b1')
    data = {
        'projects': projects,
        'document_type': document_type,
        'document_statuses': document_statuses,
        'change_order_statuses': change_order_statuses,
    }
    if request.method == 'POST':
        p = Project.objects.get(pk=request.POST.get('project'))

        d = Document()
        d.number = document_type.start + 1
        d.date = request.POST.get('date')
        d.description = request.POST.get('description')
        d.type = document_type
        d.amount = request.POST.get('amount')
        d.save()

        document_type.start += 1
        document_type.save()

        new = Change_order()
        new.status = request.POST.get('status')
        new.project = p
        new.document = d
        new.save()
        return redirect('change_order_read', pk=new.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='change_orders/read.html'):
    item = get_object_or_404(Change_order, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='change_orders/create.html'):
    update = get_object_or_404(Change_order, pk=pk)
    projects = Project.objects.filter()
    data = {
        'projects': projects,
        'change_order_statuses': change_order_statuses,
        'document_types': document_types,
        'document_statuses': document_statuses,
        'change_order_statuses': change_order_statuses,
        'item': update
    }
    if request.method == 'POST':
        update.number = request.POST.get('number')
        update.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date'), '%m/%d/%Y'), "%Y-%m-%d")
        update.description = request.POST.get('description')
        update.status = request.POST.get('status')
        update.project = Project.objects.get(pk=request.POST.get('project'))
        update.save()
        return redirect('change_order_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='change_orders/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass