import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .models import Project, General_contractor, Design_package
from resident_managers.models import Resident_manager
from project_managers.models import Project_manager
from django.contrib.auth.models import User

def index(request, template_name='projects/index.html'):
    projects = Project.objects.filter(~Q(status="DONE"))
    data = {}
    data['project_list'] = projects
    return render(request, template_name, data)

def create(request, template_name='projects/create.html'):
    pm_epi_list = User.objects.filter()
    rm_list = Resident_manager.objects.filter()
    pm_list = Project_manager.objects.filter()
    design_package_list = Design_package.objects.filter()
    general_contractor_list = General_contractor.objects.filter()
    status_type = ['Open', 'In Progress', 'Under Review', 'Approved', 'Done', 'Canceled', 'Rejected']
    data = {
        'pm_epi_list': pm_epi_list,
        'rm_list': rm_list,
        'pm_list': pm_list,
        'design_package_list': design_package_list,
        'general_contractor_list': general_contractor_list,
        'status_type': status_type,
    }
    if request.method == 'POST':
        new = Project()
        new.legal_entity = request.POST.get('legal_entity', '')
        new.portfolio = request.POST.get('portfolio', '')
        new.address = request.POST.get('address', '')
        new.unit = request.POST.get('unit', '')
        new.zip = request.POST.get('zip', '')
        new.city_state = request.POST.get('city_state', '')
        new.passwords = request.POST.get('passwords', '')
        new.bedrooms = request.POST.get('bedrooms', '')
        new.bathrooms = request.POST.get('bathrooms', '')
        new.sqFt = request.POST.get('sqFt', '')
        new.percent = request.POST.get('percent', '')
        new.jobNumber = request.POST.get('jobNumber', '')
        new.start_date = request.POST.get('start_date', '1990-01-01')
        new.end_date = request.POST.get('end_date', '1990-01-01')
        new.status = request.POST.get('status', 'Open')

        new.pm_epi = User.objects.get(id=request.POST.get('pm_epi'))
        new.rm = Resident_manager.objects.get(id=request.POST.get('rm'))
        new.pm = Project_manager.objects.get(id=request.POST.get('pm'))
        new.design_package = Design_package.objects.get(id=request.POST.get('design_package'))
        new.general_contractor = General_contractor.objects.get(id=request.POST.get('general_contractor'))

        new.save()
        return redirect('project_read', pk=new.id)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='projects/read.html'):
    item = get_object_or_404(Project, pk=pk)
    data = {}
    data['item'] = item
    return render(request, template_name, data)


def update(request, pk, template_name='projects/create.html'):
    update = get_object_or_404(Project, pk=pk)

    pm_epi_list = User.objects.filter()
    rm_list = Resident_manager.objects.filter()
    pm_list = Project_manager.objects.filter()
    design_package_list = Design_package.objects.filter()
    general_contractor_list = General_contractor.objects.filter()
    status_type = ['Open', 'In Progress', 'Under Review', 'Approved', 'Done', 'Canceled', 'Rejected']
    data = {
        'pm_epi_list': pm_epi_list,
        'rm_list': rm_list,
        'pm_list': pm_list,
        'design_package_list': design_package_list,
        'general_contractor_list': general_contractor_list,
        'status_type': status_type,
        'item': update,
    }
    if request.method == 'POST':
        update.legal_entity = request.POST.get('legal_entity', '')
        update.portfolio = request.POST.get('portfolio', '')
        update.address = request.POST.get('address', '')
        update.unit = request.POST.get('unit', '')
        update.zip = request.POST.get('zip', '')
        update.city_state = request.POST.get('city_state', '')
        update.passwords = request.POST.get('passwords', '')
        update.bedrooms = request.POST.get('bedrooms', '')
        update.bathrooms = request.POST.get('bathrooms', '')
        update.sqFt = request.POST.get('sqFt', '')
        update.percent = request.POST.get('percent', '')
        update.jobNumber = request.POST.get('jobNumber', '')
        update.start_date = request.POST.get('start_date', '1970-01-01')
        update.end_date = request.POST.get('end_date', '1970-01-01')
        update.status = request.POST.get('status', 'Open')
        update.pm_epi = User.objects.get(id=request.POST.get('pm_epi'))
        update.rm = Resident_manager.objects.get(id=request.POST.get('rm'))
        update.pm = Project_manager.objects.get(id=request.POST.get('pm'))
        update.design_package = Design_package.objects.get(id=request.POST.get('design_package'))
        update.general_contractor = General_contractor.objects.get(id=request.POST.get('general_contractor'))
        update.save()
        return redirect('project_read', pk=update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='project_managers/delete.html'):
    o = get_object_or_404(Project, pk=pk)
    o.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))