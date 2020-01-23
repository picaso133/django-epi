import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Timesheet
from projects.models import Project
from employees.models import Employ
from inspection_types.models import Inspection_type

def index(request, template_name='timesheets/index.html'):
    list = Timesheet.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='timesheets/create.html'):
    projects = Project.objects.filter()
    employees = Employ.objects.filter()
    data = {
        'projects': projects,
        'employees': employees,
    }
    if request.method == 'POST':
        new = Timesheet()
        new.date = request.POST.get('date')
        new.clock_in = request.POST.get('clock_in')
        new.clock_out = request.POST.get('clock_out')
        new.is_holiday = request.POST.get('is_holiday', False)
        new.is_weekend = request.POST.get('is_weekend', False)
        new.description = request.POST.get('description')
        new.project = Project.objects.get(pk=request.POST.get('project'))
        new.employ = Employ.objects.get(pk=request.POST.get('employ'))
        new.save()
        return redirect('timesheet_read', pk=new.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='timesheets/read.html'):
    item = get_object_or_404(Timesheet, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='timesheets/create.html'):
    update = get_object_or_404(Timesheet, pk=pk)
    projects = Project.objects.filter()
    employees = Employ.objects.filter()
    data = {
        'projects': projects,
        'employees': employees,
        'item': update
    }
    if request.method == 'POST':
        update.date = request.POST.get('date')
        update.clock_in = request.POST.get('clock_in')
        update.clock_out = request.POST.get('clock_out')
        update.is_holiday = request.POST.get('is_holiday', False)
        update.is_weekend = request.POST.get('is_weekend', False)
        update.description = request.POST.get('description')
        update.project = Project.objects.get(pk=request.POST.get('project'))
        update.employ = Employ.objects.get(pk=request.POST.get('employ'))
        update.save()
        return redirect('timesheet_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='timesheets/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass