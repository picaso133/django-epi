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
    projects = Project.objects.filter().order_by('address')
    employees = Employ.objects.filter().order_by('name')
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
        new.is_meal_time = request.POST.get('is_meal_time', False)
        new.description = request.POST.get('description')
        if request.POST.get('project'):
            new.project = Project.objects.get(pk=request.POST.get('project'))
        new.employ = Employ.objects.get(pk=request.POST.get('employ'))
        # new.save()
        return redirect('timesheet_index')
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
        update.is_meal_time = request.POST.get('is_meal_time', False)
        update.description = request.POST.get('description')
        if request.POST.get('project'):
            update.project = Project.objects.get(pk=request.POST.get('project'))
        else:
            update.project = None
        update.employ = Employ.objects.get(pk=request.POST.get('employ'))
        update.save()
        return redirect('timesheet_read', update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='timesheets/delete.html'):
    o = get_object_or_404(Timesheet, pk=pk)
    o.delete()
    return redirect('employ_read', o.employ.id)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_by_user(request, id, template_name='timesheets/create_by_user.html'):
    projects = Project.objects.filter().order_by('address')
    employee = Employ.objects.get(pk=id)
    data = {
        'projects': projects,
        'employee': employee,
    }
    if request.method == 'POST':
        new = Timesheet()
        new.date = request.POST.get('date')
        new.clock_in = request.POST.get('clock_in')
        new.clock_out = request.POST.get('clock_out')
        new.is_holiday = request.POST.get('is_holiday', False)
        new.is_weekend = request.POST.get('is_weekend', False)
        new.is_meal_time = request.POST.get('is_meal_time', False)
        new.description = request.POST.get('description')
        if request.POST.get('project'):
            new.project = Project.objects.get(pk=request.POST.get('project'))
        new.employ = employee
        new.save()
        return redirect('employ_read', employee.id)
    else:
        return render(request, template_name, data)