import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Inspection_type

def index(request, template_name='inspection_types/index.html'):
    inspection_types = Inspection_type.objects.filter()
    data = {}
    data['list'] = inspection_types
    return render(request, template_name, data)

def create(request, template_name='inspection_types/create.html'):
    if request.method == 'POST':
        new = Inspection_type()
        new.name = request.POST.get('name', '')
        new.code = request.POST.get('code', '')
        new.category = request.POST.get('category', '')
        new.save()
        return redirect('inspection_type_index')
    else:
        return render(request, template_name)
    # pass

def read(request, pk, template_name='inspection_types/read.html'):
    # employ = get_object_or_404(Check, pk=pk)
    # data = {}
    # data['employ'] = employ
    # return render(request, template_name, data)
    pass

def update(request, pk, template_name='inspection_types/create.html'):
    update = get_object_or_404(Inspection_type, pk=pk)
    if request.method == 'POST':
        update.name = request.POST.get('name', '')
        update.code = request.POST.get('code', '')
        update.category = request.POST.get('category', '')
        update.save()
        return redirect('check_index')
    return render(request, template_name, {'inspection_type': update})
    pass

def delete(request, pk, template_name='inspection_types/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass