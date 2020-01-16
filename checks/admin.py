from django.contrib import admin
from .models import Check

class CheckAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'pay_to', 'pay_for', 'description', 'amount')
    search_fields = ['number', 'date', 'pay_to', 'pay_for', 'description', 'amount']
    ordering = ['number']

admin.site.register(Check, CheckAdmin)