import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Check

def index(request, template_name='checks/index.html'):
    checks = Check.objects.filter()
    data = {}
    data['check_list'] = checks
    return render(request, template_name, data)

def create(request, template_name='checks/create.html'):
    if request.method == 'POST':
        newCheck = Check()
        newCheck.number = request.POST.get('number', '')
        if request.POST.get('date', '') != "":
            newCheck.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date', ''), '%m/%d/%Y'),"%Y-%m-%d")
        else:
            newCheck.date = datetime.date.strftime(datetime.datetime.strptime("01/01/1970", '%m/%d/%Y'),"%Y-%m-%d")
        newCheck.pay_to = request.POST.get('pay_to', '')
        newCheck.pay_for = request.POST.get('pay_for', '')
        newCheck.description = request.POST.get('description', '')
        newCheck.amount = request.POST.get('amount', '')
        newCheck.save()

        return redirect('check_index')
    else:
        return render(request, template_name)

def read(request, pk, template_name='checks/read.html'):
    # employ = get_object_or_404(Check, pk=pk)
    # data = {}
    # data['employ'] = employ
    # return render(request, template_name, data)
    pass

def update(request, pk, template_name='checks/create.html'):
    check = get_object_or_404(Check, pk=pk)
    if request.method == 'POST':
        check.number = request.POST.get('number', '')
        check.date = datetime.date.strftime(datetime.datetime.strptime(request.POST.get('date', ''), '%m/%d/%Y'),"%Y-%m-%d")
        check.pay_to = request.POST.get('pay_to', '')
        check.pay_for = request.POST.get('pay_for', '')
        check.description = request.POST.get('description', '')
        check.amount = request.POST.get('amount', '')
        check.save()
        return redirect('check_index')
    return render(request, template_name, {'check': check})

def delete(request, pk, template_name='checks/delete.html'):
    check = get_object_or_404(Check, pk=pk)
    check.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))