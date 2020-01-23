import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Order
from projects.models import Project
from suppliers.models import Supplier
from inspection_types.models import Inspection_type

def index(request, template_name='orders/index.html'):
    list = Order.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='orders/create.html'):
    projects = Project.objects.filter()
    suppliers = Supplier.objects.filter()
    data = {
        'projects': projects,
        'suppliers': suppliers,
        'statuses': ['Pending', 'Awaiting Payment', 'Awaiting Fulfillment', 'Awaiting Shipment',
            'Awaiting Pickup', 'Partially Shipped', 'Completed', 'Shipped', 'Canceled',
            'Declined', 'Refunded', 'Disputed', 'Manual Verification Required', 'Partially Refunded'
        ]
    }
    if request.method == 'POST':
        new = Order()
        new.number = request.POST.get('number')
        new.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date'),'%m/%d/%Y'),"%Y-%m-%d")
        new.description = request.POST.get('description')
        new.status = request.POST.get('status')
        new.project = Project.objects.get(pk=request.POST.get('project'))
        new.supplier = Supplier.objects.get(pk=request.POST.get('supplier'))
        new.save()
        return redirect('order_read', pk=new.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='orders/read.html'):
    item = get_object_or_404(Order, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='orders/create.html'):
    update = get_object_or_404(Order, pk=pk)
    projects = Project.objects.filter()
    suppliers = Supplier.objects.filter()
    data = {
        'projects': projects,
        'suppliers': suppliers,
        'statuses': ['Pending', 'Awaiting Payment', 'Awaiting Fulfillment', 'Awaiting Shipment',
            'Awaiting Pickup', 'Partially Shipped', 'Completed', 'Shipped', 'Canceled',
            'Declined', 'Refunded', 'Disputed', 'Manual Verification Required', 'Partially Refunded'
        ],
        'item': update
    }
    if request.method == 'POST':
        update.number = request.POST.get('number')
        update.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date'), '%m/%d/%Y'), "%Y-%m-%d")
        update.description = request.POST.get('description')
        update.status = request.POST.get('status')
        update.project = Project.objects.get(pk=request.POST.get('project'))
        update.supplier = Supplier.objects.get(pk=request.POST.get('supplier'))
        update.save()
        return redirect('order_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='orders/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass