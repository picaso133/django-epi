import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Files_storage
from employees.models import Employ
from change_orders.models import Change_order
from orders.models import Order
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage

def upload_file(request, key):
    myfile = request.FILES[key]
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    return Files_storage.objects.create(file=filename, description=request.POST.get('description'))

def zip_export(module, id):
    # se extrag toate fisierele din modul si se arhiveaza
    # denumirea relatiei de extragere a fisierelor din modul poate fi diferita pentru fiecare in parte
    pass

def delete_os_fie(file):
    # trebuie sa am un array cu toate modulele care folosesc files_storage
    # trebuie de verificat daca fisierul de intrare se utilizeaza in restu modulelor prin incrementarea unui k
    # daca k este mai mare de 1 inseamna ca fisierul are relatii si cu alte module si nu trebuie stere
    # daca k este 1 fisierul poate fi sters in siguranta
    pass


def delete(request, pk):
    file = get_object_or_404(Files_storage, pk=pk)
    file_path = file.file_path()
    file.delete()
    os.remove(file_path)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def assign(request, module, id, template_name = 'file_storage/upload.html'):
    if request.method == 'POST':
        if module == 'employ':
            employ = get_object_or_404(Employ, pk=id)
            employ.documents.add(upload_file(request, 'file'))
            employ.save()
        if module == 'change_order':
            change_order = get_object_or_404(Change_order, pk=id)
            change_order.files.add(upload_file(request, 'file'))
            change_order.save()
        if module == 'order':
            order = get_object_or_404(Order, pk=id)
            order.files.add(upload_file(request, 'file'))
            order.save()
        return HttpResponse('<script type="text/javascript">window.close()</script>')
    else:
        return render(request, template_name)