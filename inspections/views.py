import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Inspection
from projects.models import Project
from inspection_types.models import Inspection_type

def index(request, template_name='inspections/index.html'):
    inspections = Inspection.objects.filter()
    data = {}
    data['list'] = inspections
    return render(request, template_name, data)

def create(request, template_name='inspections/create.html'):
    projects = Project.objects.filter()
    inspection_types = Inspection_type.objects.filter()
    data = {}
    data['projects'] = projects
    data['inspection_types'] = inspection_types
    data['statuses'] = ['Passed', 'Failed', 'Partial', 'Scheduled']
    if request.method == 'POST':
        new = Inspection()
        new.name = request.POST.get('name', '')
        new.code = request.POST.get('code', '')
        new.confirmation_number = request.POST.get('confirmation_number', '')
        new.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date', ''), '%m/%d/%Y'),"%Y-%m-%d")
        new.category = request.POST.get('category', '')

        new.type = Inspection_type.objects.get(pk=request.POST.get('type', ''))
        new.project = Project.objects.get(pk=request.POST.get('project', ''))

        new.save()
        return redirect('inspection_type_index')
    else:
        return render(request, template_name, data)
    # pass

def read(request, pk, template_name='inspections/read.html'):
    # employ = get_object_or_404(Check, pk=pk)
    # data = {}
    # data['employ'] = employ
    # return render(request, template_name, data)
    pass

def update(request, pk, template_name='inspections/create.html'):
    projects = Project.objects.filter()
    inspection_types = Inspection_type.objects.filter()
    update = get_object_or_404(Inspection, pk=pk)

    data = {}
    data['projects'] = projects
    data['inspection_types'] = inspection_types
    data['inspection'] = update
    data['statuses'] = Inspection.status_type
    if request.method == 'POST':
        update.name = request.POST.get('name')
        update.code = request.POST.get('code')
        update.confirmation_number = request.POST.get('confirmation_number')
        update.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date'), '%m/%d/%Y'),"%Y-%m-%d")
        update.category = request.POST.get('category')

        update.type = Inspection_type.objects.get(pk=request.POST.get('type', ''))
        update.project = Project.objects.get(pk=request.POST.get('project', ''))
        update.save()
        return redirect('inspection_index')
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='inspections/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass