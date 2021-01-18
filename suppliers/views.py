import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Supplier
from customers.models import Customer

def index(request, template_name='suppliers/index.html'):
    list = Supplier.objects.filter()
    data = {
        'list': list
    }

    # for e in list:
    #     Customer(name=e.name, address=e.address, email=e.contact_email, phone=e.contact_phone, supplier=e).save()

    return render(request, template_name, data)

def create(request, template_name='suppliers/create.html'):
    if request.method == 'POST':
        new = Supplier()
        new.name = request.POST.get('name')
        new.address = request.POST.get('address')
        new.contact_name = request.POST.get('contact_name')
        new.contact_phone = request.POST.get('contact_phone')
        new.contact_phone = request.POST.get('contact_phone')
        new.address = request.POST.get('address')
        new.save()

        Customer(name=new.name, address=new.address, email=new.contact_email, phone=new.contact_phone, supplier=new).save()
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
        update.address = request.POST.get('address')
        update.save()
        return redirect('supplier_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='suppliers/delete.html'):
    o = get_object_or_404(Supplier, pk=pk)
    o.delete()
    return redirect('supplier_index')