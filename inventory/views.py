import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Inventory, Inventory_category
from file_storage.models import Files_storage
from file_storage.views import upload_file

def index(request, template_name='inventory/index.html'):
    list = Inventory.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='inventory/create.html'):
    categories = Inventory_category.objects.filter()
    data = {
        'categories': categories
    }
    if request.method == 'POST':
        new = Inventory()
        new.name = request.POST.get('name')
        new.qty = request.POST.get('qty')
        new.number = request.POST.get('number')
        new.description = request.POST.get('description')
        new.category = Inventory_category.objects.get(pk=request.POST.get('category'))
        new.file = upload_file(request, 'file')
        new.save()
        return redirect('inventory_read', pk=new.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='inventory/read.html'):
    item = get_object_or_404(Inventory, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='inventory/create.html'):
    update = get_object_or_404(Inventory, pk=pk)
    categories = Inventory_category.objects.filter()
    data = {
        'categories': categories,
        'item': update
    }
    if request.method == 'POST':
        update.name = request.POST.get('name')
        update.qty = request.POST.get('qty')
        update.number = request.POST.get('number')
        update.description = request.POST.get('description')
        update.category = Inventory_category.objects.get(pk=request.POST.get('category'))
        update.file = upload_file(request, 'file')
        update.save()
        return redirect('inventory_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='inventory/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass