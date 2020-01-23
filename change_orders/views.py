from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Change_order
from projects.models import Project
from inspection_types.models import Inspection_type

def index(request, template_name='change_orders/index.html'):
    list = Change_order.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='change_orders/create.html'):
    projects = Project.objects.filter()
    data = {
        'projects': projects,
        'statuses': ['Open', 'Sent', 'Under Review', 'Approved', 'Rejected', 'Canceled']
    }
    if request.method == 'POST':
        new = Change_order()
        new.number = request.POST.get('number')
        new.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date'),'%m/%d/%Y'),"%Y-%m-%d")
        new.description = request.POST.get('description')
        new.status = request.POST.get('status')
        new.project = Project.objects.get(pk=request.POST.get('project'))
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
        'statuses': ['Open', 'Sent', 'Under Review', 'Approved', 'Rejected', 'Canceled'],
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