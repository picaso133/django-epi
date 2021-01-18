import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from .models import Permit
from projects.models import Project
from file_storage.models import Files_storage

def upload_file(request, key):
    try:
        myfile = request.FILES[key]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        return Files_storage.objects.create(file=filename)
    except:
        return False

def index(request, template_name='permits/index.html'):
    list = Permit.objects.filter()
    data = {}
    data['list'] = list
    return render(request, template_name, data)

def create(request, template_name='permits/create.html'):
    data = {}
    projects = Project.objects.filter()
    data['projects'] = projects
    data['types'] = ['Electric', 'Plumbing', 'Building', 'Parking']
    if request.method == 'POST':
        new = Permit()
        new.number = request.POST.get('number', '')
        new.type = request.POST.get('type', '')
        new.description = request.POST.get('description', '')
        if request.POST.get('start_date') != "":
            new.start_date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('start_date'), '%m/%d/%Y'),"%Y-%m-%d")
        if request.POST.get('end_date') != "":
            new.end_date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('end_date'), '%m/%d/%Y'),"%Y-%m-%d")

        new.file = upload_file(request, 'file')
        new.project = Project.objects.get(pk=request.POST.get('project', ''))

        new.save()
        return redirect('permit_index')
    else:
        return render(request, template_name, data)
    # pass

def read(request, pk, template_name='permits/read.html'):
    item = get_object_or_404(Permit, pk=pk)
    data = {}
    data['item'] = item
    return render(request, template_name, data)


def update(request, pk, template_name='permits/create.html'):
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

def delete(request, pk):
    o = get_object_or_404(Permit, pk=pk)
    o.delete()
    return redirect('permit_index')