import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Supplier

def index(request, template_name='suppliers/index.html'):
    list = Supplier.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='suppliers/create.html'):
    if request.method == 'POST':
        new = Supplier()
        new.name = request.POST.get('name')
        new.contact_name = request.POST.get('contact_name')
        new.contact_phone = request.POST.get('contact_phone')
        new.contact_email = request.POST.get('contact_email')
        new.save()
        return redirect('supplier_read', pk=new.id)
    else:
        return render(request, template_name)

def read(request, pk, template_name='suppliers/read.html'):
    item = get_object_or_404(Supplier, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='suppliers/create.html'):
    update = get_object_or_404(Supplier, pk=pk)
    data = {
        'item': update
    }
    if request.method == 'POST':
        update.name = request.POST.get('name')
        update.contact_name = request.POST.get('contact_name')
        update.contact_phone = request.POST.get('contact_phone')
        update.contact_email = request.POST.get('contact_email')
        update.save()
        return redirect('supplier_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='suppliers/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass