from __future__ import unicode_literals

from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.db import models

from .models import Employ, User, Files_storage
from timesheets.models import Timesheet
from customers.models import Customer

@require_POST
def upload_file(request, key):
    myfile = request.FILES[key]
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    file_in_storage = Files_storage.objects.create(file=filename)
    return file_in_storage

def index(request, template_name='employees/index.html'):
    employees = Employ.objects.filter().order_by('name')
    # employees = Employ.objects.filter(is_active=True)
    inactive_employes = Employ.objects.filter(is_active=False)

    data = {
        'employ_list': employees,
        'inactive_count': inactive_employes.count()
    }

    # for e in employees:
    #     Customer(name=e.name, address=e.address, email=e.email, phone=e.phone, employ=e).save()

    return render(request, template_name, data)

def create(request, template_name='employees/create.html'):
    if request.method == 'POST':
        new = Employ()
        new.name = request.POST.get('name', '')
        new.phone = request.POST.get('phone', '')
        new.address = request.POST.get('address', '')
        new.email = request.POST.get('email', '')
        if request.POST.get('user') != '':
            new.user = User.objects.get(id=request.POST.get('user'))
        if request.POST.get('is_active') == 'on':
            new.is_active = True
        else:
            new.is_active = False
        new.save()

        Customer(name=new.name, address=new.address, email=new.email, phone=new.phone, employ=new).save()
        return redirect('employ_index')
    else:
        return render(request, template_name)

def read(request, pk, template_name='employees/read.html'):
    employ = get_object_or_404(Employ, pk=pk)
    timesheets = Timesheet.objects.filter(employ_id=pk).order_by('date')
    data = {
        'employ': employ,
        'timesheets': timesheets
    }
    return render(request, template_name, data)

def update(request, pk, template_name='employees/create.html'):
    employ = get_object_or_404(Employ, pk=pk)
    if request.method == 'POST':
        employ.name = request.POST.get('name', '')
        employ.phone = request.POST.get('phone', '')
        employ.address = request.POST.get('address', '')
        employ.email = request.POST.get('email', '')
        if request.POST.get('user') != '':
            employ.user = User.objects.get(id=request.POST.get('user'))
        if request.POST.get('is_active') == 'on':
            employ.is_active = True
        else:
            employ.is_active = False
        employ.save()

        # newEmploy.documents.add(upload_file(request, 'id_document'))
        # newEmploy.documents.add(upload_file(request, 'contract'))
        employ.save()
        return redirect('employ_index')
    return render(request, template_name, {'employ': employ})

def delete(request, pk, template_name='employees/delete.html'):
    employ = get_object_or_404(Employ, pk=pk)
    employ.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def assign_files(request,pk, template_name='file_storage/upload.html'):
    employ = get_object_or_404(Employ, pk=pk)
    employ.documents.add()
    return render(request, template_name)