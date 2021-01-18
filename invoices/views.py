from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from change_orders.models import Change_order
from .models import Invoice
from invoice_items.models import Invoice_item
from projects.models import Project
from documents.models import Document, Document_type
from documents.views import document_types, document_statuses
from customers.models import Customer

change_order_statuses = ['Open', 'Sent', 'Under Review', 'Approved', 'Rejected', 'Canceled']

def index(request, template_name='invoices/index.html'):
    list = Invoice.objects.filter()
    data = {
        'list': list
    }
    return render(request, template_name, data)

def create(request, template_name='invoices/create.html'):
    items = []
    customers = Customer.objects.filter()
    document_type = Document_type.objects.get(uuid='5b34bfb8f43e436aa57e044b3c5e1824')
    data = {
        'customers': customers,
        'document_type': document_type,
        'document_statuses': document_statuses,
        'document_status': 'Draft',
    }
    if request.method == 'POST':
        temp = []
        print(request.POST)
        for v in request.POST:
            if v.find('item') == 0:
                temp.append(v[5:v.find(']')])
        elms = list(dict.fromkeys(temp))
        for e in elms:
            print(request.POST.get('item[' + e + '][id]'))
            if request.POST.get('item[' + e + '][id]'):
                v = Invoice_item.objects.get(pk = request.POST.get('item[' + e + '][id]'))
                i = {
                    'description': v.description,
                    'unit_price': v.unit_price,
                    'qty': v.qty,
                }
            else:
                i = {
                    'description': request.POST.get('item[' + e + '][description]'),
                    'unit_price': request.POST.get('item[' + e + '][unit_price]'),
                    'qty': request.POST.get('item[' + e + '][qty]'),
                }

            items.append(i)

        d = Document()
        d.number = document_type.start + 1
        d.date = request.POST.get('date')
        d.description = request.POST.get('description')
        d.type = document_type
        d.document = request.POST.get('status')
        # d.amount = request.POST.get('amount')
        d.save()
        # print(str(d))
        document_type.start += 1
        document_type.save()

        i = Invoice()
        i.due_date = request.POST.get('due_date')
        i.document = d
        i.customer = Customer.objects.get(pk=request.POST.get('customer'))
        i.save()
        print(i)

        sum = 0

        for item in items:
            # if item['id']:
            #     ii = Invoice_item.objects.get(pk=item['id'])
            # else:
            ii = Invoice_item()
            ii.description = item.get('description')
            ii.unit_price = float(item.get('unit_price'))
            ii.qty = float(item.get('qty'))
            ii.amount = ii.unit_price * ii.qty
            ii.invoice = i
            ii.save()
            print(ii)
            sum += ii.amount

        d.amount = sum
        d.save()
        # print(str(d))

        return redirect('invoice_read', pk=i.id)
        # return render(request, template_name, data)
    else:
        return render(request, template_name, data)

def read(request, pk, template_name='invoices/read.html'):
    item = get_object_or_404(Invoice, pk=pk)
    data = {
        'item': item
    }
    return render(request, template_name, data)

def update(request, pk, template_name='invoices/create.html'):
    update = get_object_or_404(Invoice, pk=pk)
    items = []
    customers = Customer.objects.filter()
    document_type = Document_type.objects.get(uuid='5b34bfb8f43e436aa57e044b3c5e1824')
    data = {
        'customers': customers,
        'document_type': document_type,
        'document_statuses': document_statuses,
        'document_status': 'Draft',
        'item': update
    }
    if request.method == 'POST':
        temp = []
        print(request.POST)
        for v in request.POST:
            if v.find('item') == 0:
                temp.append(v[5:v.find(']')])
        elms = list(dict.fromkeys(temp))
        for e in elms:
            i = {
                'description': request.POST.get('item[1][description]'),
                'unit_price': request.POST.get('item[1][unit_price]'),
                'qty': request.POST.get('item[1][qty]'),
            }
            items.append(i)

        d = update.document
        d.number = document_type.start + 1
        d.date = request.POST.get('date')
        d.description = request.POST.get('description')
        d.type = document_type
        # d.amount = request.POST.get('amount')
        d.save()
        document_type.start += 1
        document_type.save()

        update.due_date = request.POST.get('due_date')
        update.document = d
        update.customer = Customer.objects.get(pk=request.POST.get('customer'))
        update.save()

        sum = 0
        for item in items:
            ii = Invoice_item()
            ii.description = item.get('description')
            ii.unit_price = float(item.get('unit_price'))
            ii.qty = float(item.get('qty'))
            ii.amount = ii.unit_price * ii.qty
            ii.invoice = i
            ii.save()
            sum += ii.amount

        print(sum)
        d.amount = sum
        d.save()

        # return redirect('change_order_read', pk=new.id)
        return render(request, template_name, data)
    else:
        return render(request, template_name, data)

def delete(request, pk, template_name='change_orders/delete.html'):
    check = get_object_or_404(Invoice, pk=pk)
    check.delete()
    return redirect('invoice_index')