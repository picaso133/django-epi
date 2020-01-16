from django.shortcuts import render, redirect, get_object_or_404
from .models import Files_storage
from employees.models import Employ
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

def upload_file(request, key):
    myfile = request.FILES[key]
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    return Files_storage.objects.create(file=filename)

def delete(request, pk):
    file = get_object_or_404(Files_storage, pk=pk)
    file.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def assign(request, module, id, template_name = 'file_storage/upload.html'):
    if request.method == 'POST':
        if module == 'employ':
            employ = get_object_or_404(Employ, pk=id)
            employ.documents.add(upload_file(request, 'file'))
            employ.save()
        return HttpResponse('<script type="text/javascript">window.close()</script>')
    else:
        return render(request, template_name)