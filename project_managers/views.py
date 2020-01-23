import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from .models import Project_manager
from projects.models import Project
from file_storage.models import Files_storage


def index(request, template_name='project_managers/index.html'):
    list = Project_manager.objects.filter()
    data = {}
    data['list'] = list
    return render(request, template_name, data)

def create(request, template_name='project_managers/create.html'):
    if request.method == 'POST':
        new = Project_manager()
        new.name = request.POST.get('name', '')
        new.phone = request.POST.get('phone', '')
        new.email = request.POST.get('email', '')
        new.save()
        return redirect('resident_manager_index')
    else:
        return render(request, template_name)

def read(request, pk, template_name='project_managers/read.html'):
    item = get_object_or_404(Project_manager, pk=pk)
    data = {}
    data['item'] = item
    return render(request, template_name, data)


def update(request, pk, template_name='project_managers/create.html'):
    update = get_object_or_404(Permit, pk=pk)

    data = {}
    projects = Project.objects.filter()
    data['projects'] = projects
    data['types'] = ['Electric', 'Plumbing', 'Building', 'Parking']
    data['item'] = update
    if request.method == 'POST':
        update.number = request.POST.get('number', '')
        update.type = request.POST.get('type', '')
        update.description = request.POST.get('description', '')
        if request.POST.get('start_date') != "":
            update.start_date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('start_date'), '%m/%d/%Y'), "%Y-%m-%d")
        if request.POST.get('end_date') != "":
            update.end_date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('end_date'), '%m/%d/%Y'),"%Y-%m-%d")
        file = upload_file(request, 'file')
        if file != False:
            update.file = file
        update.project = Project.objects.get(pk=request.POST.get('project', ''))
        update.save()
        return redirect('permit_index')
    return render(request, template_name, data)
    pass

def delete(request, pk, template_name='project_managers/delete.html'):
    # check = get_object_or_404(Check, pk=pk)
    # check.delete()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass