import datetime
from operator import itemgetter

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .models import Work_log, Work_log_types
from employees.models import Employ
from projects.models import Project, General_contractor, Design_package
from resident_managers.models import Resident_manager
from project_managers.models import Project_manager
from django.contrib.auth.models import User
import itertools

def index(request, template_name='work_logs/index.html'):
    list = Work_log.objects.all()
    data = {
        'list': list,
    }
    return render(request, template_name, data)

def create(request, template_name='work_logs/create.html'):
    projects = Project.objects.filter()
    employees = Employ.objects.filter()
    categories = Work_log_types.objects.filter()
    statuses = ['Holding', 'Prioritized', 'Started', 'Finished']
    data = {
        'projects': projects,
        'employees': employees,
        'categories': categories,
        'statuses': statuses,
    }
    if request.method == 'POST':
        new = Work_log()
        new.start_date = request.POST.get('start_date', '1970-01-01 00:00:00')
        new.end_date = request.POST.get('end_date', '1970-01-01 00:00:00')
        new.title = request.POST.get('title')
        new.description = request.POST.get('description')
        new.status = request.POST.get('status')

        new.project = Project.objects.get(pk=request.POST.get('project'))
        new.work_log_type = Work_log_types.objects.get(pk=request.POST.get('category'))
        new.save()

        for employee in request.POST.getlist('employees'):
            new.employees.add(Employ.objects.get(pk=employee))


        # return redirect('timesheet_read', pk=new.id)
        return redirect('work_log_index')
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='work_logs/read.html'):
    item = get_object_or_404(Work_log, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='work_logs/create.html'):
    update = get_object_or_404(Work_log, pk=pk)
    projects = Project.objects.filter()
    employees = Employ.objects.filter()
    categories = Work_log_types.objects.filter()
    statuses = ['Holding', 'Prioritized', 'Started', 'Finished']
    data = {
        'projects': projects,
        'employees': employees,
        'categories': categories,
        'statuses': statuses,
        'item': update
    }
    if request.method == 'POST':
        update.start_date = request.POST.get('start_date', '1970-01-01 00:00:00')
        update.end_date = request.POST.get('end_date', '1970-01-01 00:00:00')
        update.title = request.POST.get('title')
        update.description = request.POST.get('description')
        update.status = request.POST.get('status')

        update.project = Project.objects.get(pk=request.POST.get('project'))
        update.work_log_type = Work_log_types.objects.get(pk=request.POST.get('category'))
        update.save()

        for employee in update.employees.all():
            update.employees.remove(employee)

        for employee in request.POST.getlist('employees'):
            update.employees.add(Employ.objects.get(pk=employee))


        return redirect('work_log_index')
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='timesheets/delete.html'):
    o = get_object_or_404(Work_log, pk=pk)
    o.delete()
    return redirect('work_log_index')
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))