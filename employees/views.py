from __future__ import unicode_literals

from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.db import models

from .models import Employ, User, Files_storage
# Create your views here.

class EmployesForm(ModelForm):
    class Meta:
        model = Employ
        fields = ['id', 'name', 'phone', 'address', 'email', 'documents']

@require_POST
def upload_file(request, key):
    myfile = request.FILES[key]
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    file_in_storage = Files_storage.objects.create(file=filename)
    return file_in_storage

def index(request, template_name='employees/index.html'):
    employes = Employ.objects.filter()
    # employees = Employ.objects.filter(is_active=True)
    inactive_employes = Employ.objects.filter(is_active=False)
    data = {}
    data['employ_list'] = employes
    data['inactive_count'] = inactive_employes.count()
    return render(request, template_name, data)

def create(request, template_name='employees/create.html'):
    if request.method == 'POST':
        newEmploy = Employ()
        newEmploy.name = request.POST.get('name', '')
        newEmploy.phone = request.POST.get('phone', '')
        newEmploy.address = request.POST.get('address', '')
        newEmploy.email = request.POST.get('email', '')
        if request.POST.get('user') != '':
            newEmploy.user = User.objects.get(id=request.POST.get('user'))
        if request.POST.get('is_active') == 'on':
            newEmploy.is_active = True
        else:
            newEmploy.is_active = False
        newEmploy.save()

        return redirect('employ_index')
    else:
        return render(request, template_name)

def read(request, pk, template_name='employees/read.html'):
    employ = get_object_or_404(Employ, pk=pk)
    data = {}
    data['employ'] = employ
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