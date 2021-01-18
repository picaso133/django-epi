import datetime
import uuid
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db.models import Q
from .models import Project, General_contractor, Design_package
from resident_managers.models import Resident_manager
from project_managers.models import Project_manager
from django.contrib.auth.models import User
from file_storage.views import upload_file
from documents.models import Document
from customers.models import Customer


def index(request, template_name='projects/index.html'):
    projects = Project.objects.filter(~Q(status="Done"))
    data = {
        'project_list': projects
    }

    # for p in projects:
    #     Customer(name=p.get_name(), address=p.get_address(), email='', phone='', project=p).save()

    return render(request, template_name, data)

def index_inactive(request, template_name='projects/index.html'):
    projects = Project.objects.filter(status="Done")
    data = {'project_list': projects}
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
        new.legal_entity = request.POST.get('legal_entity', None)
        new.portfolio = request.POST.get('portfolio', None)
        new.address = request.POST.get('address', None)
        new.unit = request.POST.get('unit', None)
        new.zip = request.POST.get('zip', None)
        new.city_state = request.POST.get('city_state', None)
        new.passwords = request.POST.get('passwords', None)
        new.bedrooms = request.POST.get('bedrooms', None)
        new.bathrooms = request.POST.get('bathrooms', None)
        new.sqFt = request.POST.get('sqFt', None)
        new.percent = request.POST.get('percent', None)
        new.jobNumber = request.POST.get('jobNumber', '')
        # new.jobNumber = uuid.uuid4()
        new.start_date = request.POST.get('start_date', None)
        new.end_date = request.POST.get('end_date', None)
        new.status = request.POST.get('status', 'Open')

        if request.POST.get('pm_epi'):
            new.pm_epi = User.objects.get(id=request.POST.get('pm_epi'))
        if request.POST.get('rm'):
            new.rm = Resident_manager.objects.get(id=request.POST.get('rm'))
        if request.POST.get('pm'):
            new.pm = Project_manager.objects.get(id=request.POST.get('pm'))
        if request.FILES.get('rq'):
            new.rq = upload_file(request, 'rq')
        if request.FILES.get('contract'):
            new.contract = upload_file(request, 'contract')
        if request.FILES.get('proposal'):
            new.proposal = upload_file(request, 'proposal')
        if request.POST.get('design_package'):
            new.design_package = Design_package.objects.get(id=request.POST.get('design_package'))
        if request.POST.get('general_contractor'):
            new.general_contractor = General_contractor.objects.get(id=request.POST.get('general_contractor'))
        new.save()

        Customer(name=new.get_name(), address=new.get_address(), email='', phone='', project=new).save()
        # return redirect('project_read', pk=new.id)
        return redirect('project_index')
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='projects/read.html'):
    item = get_object_or_404(Project, pk=pk)
    documents = Document.objects.all();
    data = {
        'item': item,
        'documents': documents,
    }
    if request.method == 'POST':
        if request.POST.get('document'):
            item.documents.add(Document.objects.get(pk=request.POST.get('document')))
            item.save()

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
        update.legal_entity = request.POST.get('legal_entity', None)
        update.portfolio = request.POST.get('portfolio', None)
        update.address = request.POST.get('address', None)
        update.unit = request.POST.get('unit', None)
        update.zip = request.POST.get('zip', None)
        update.city_state = request.POST.get('city_state', None)
        update.passwords = request.POST.get('passwords', None)
        update.bedrooms = request.POST.get('bedrooms', None)
        update.bathrooms = request.POST.get('bathrooms', None)
        update.sqFt = request.POST.get('sqFt', None)
        update.percent = request.POST.get('percent', None)
        update.jobNumber = request.POST.get('jobNumber', '')
        # new.jobNumber = uuid.uuid4()
        update.start_date = request.POST.get('start_date', None)
        update.end_date = request.POST.get('end_date', None)
        update.status = request.POST.get('status', 'Open')

        if request.POST.get('pm_epi'):
            update.pm_epi = User.objects.get(id=request.POST.get('pm_epi'))
        if request.POST.get('rm'):
            update.rm = Resident_manager.objects.get(id=request.POST.get('rm'))
        if request.POST.get('pm'):
            update.pm = Project_manager.objects.get(id=request.POST.get('pm'))
        if request.FILES.get('rq'):
            update.rq = upload_file(request, 'rq')
        if request.FILES.get('contract'):
            update.contract = upload_file(request, 'contract')
        if request.FILES.get('proposal'):
            update.proposal = upload_file(request, 'proposal')
        if request.POST.get('design_package'):
            update.design_package = Design_package.objects.get(id=request.POST.get('design_package'))
        if request.POST.get('general_contractor'):
            update.general_contractor = General_contractor.objects.get(id=request.POST.get('general_contractor'))

        update.save()
        return redirect('project_read', pk=update.id)
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='project_managers/delete.html'):
    o = get_object_or_404(Project, pk=pk)
    o.delete()
    return redirect('project_index')
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def api_get(request):
    projects = Project.objects.filter(~Q(status="Done"))
    return HttpResponse(serializers.serialize('json', projects), content_type="text/json-comment-filtered")