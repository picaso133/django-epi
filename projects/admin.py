# from django.contrib import admin
# from .models import Project, Project_managers, Resident_managers, Design_package, General_contractor, Permit, Inspection, Inspection_type
#
# class rmView(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'phone')
#     search_fields = ['first_name', 'last_name', 'phone']
#     fieldsets = (
#         ('Information', {
#             'classes': ('wide', 'extrapretty'),
#             'fields': ['company', ('first_name', 'last_name')]
#         }),
#         ('Info', {
#             'classes': ('collapse',),
#             'fields': ('phone', 'email')
#         })
#     )
#
# class pmView(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'phone')
#     search_fields = ['first_name', 'last_name', 'phone']
#     fieldsets = (
#         ('Information', {
#             'classes': ('wide', 'extrapretty'),
#             'fields': ['company', ('first_name', 'last_name')]
#         }),
#         ('Info', {
#             'classes': ('collapse',),
#             'fields': ('phone', 'email')
#         })
#     )
#
# class general_contractorView(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'company', 'phone')
#     search_fields = ['first_name', 'last_name', 'company', 'phone']
#     fieldsets = (
#         ('Information', {
#             'classes': ('wide', 'extrapretty'),
#             'fields': ['company', ('first_name', 'last_name')]
#         }),
#         ('Info', {
#             'classes': ('collapse',),
#             'fields': ('phone', ('email', 'order_email'))
#         })
#     )
#
# class deign_packageView(admin.ModelAdmin):
#     list_display = ('type',)
#     search_fields = ['type']
#
# class permitView(admin.ModelAdmin):
#     list_display = ('number', 'type', 'file')
#     search_fields = ['type', 'number']
#
# class inspection_typeView(admin.ModelAdmin):
#     list_display = ('name', 'code', 'category')
#     search_fields = ['code', 'name', 'category']
#
# class inspectionView(admin.ModelAdmin):
#     list_display = ('type', 'url', 'date', 'confirmation_number', 'status', 'project')
#     search_fields = ['confirmation_number']
#     autocomplete_fields = ['type', 'project']
#     list_filter = ['status']
#     ordering = ['date']
#
# class InlinePermit(admin.TabularInline):
#     model = Project.permits.through
#     extra = 0
#
#
# # class InlineInspections(admin.TabularInline):
# #     model = Inspection.project
# #     extra = 0
#
# class projectView(admin.ModelAdmin):
#     inlines = [InlinePermit]
#     list_display = ('jobNumber', 'address', 'status', 'percent', 'inspections', 'uuid')
#     search_fields = ['address', 'uuid', 'jobNumber']
#     autocomplete_fields = ['drawings', 'rm', 'pm', 'pm_epi', 'design_package', 'general_contractor', 'permits']
#     fieldsets = (
#         ('Location Information', {
#             'classes': ('wide', 'extrapretty'),
#             'fields': (('jobNumber', 'percent'),('legal_entity','portfolio'), ('address', 'passwords'), ('bedrooms','bathrooms', 'sqFt'),'rm')
#         }),
#         ('Project Manager EPI', {
#             # 'classes': ('collapse',),
#             'fields': ('pm_epi',),
#         }),
#         ('Project Manager', {
#             # 'classes': ('collapse',),
#             'fields': ('pm',),
#         }),
#         ('Dates', {
#             'classes': ('collapse',),
#             'fields': [('start_date', 'end_date')]
#         }),
#         ('Design Package', {
#             'classes': ('collapse',),
#             'fields': ('design_package',)
#         }),
#         ('General Contractor', {
#             'classes': ('collapse',),
#             'fields': ('general_contractor',)
#         }),
#         ('Drawings', {
#             'classes': ('collapse',),
#             'fields': ('drawings',)
#         }),
#         # ('Permits', {
#         #     'classes': ('collapse',),
#         #     'fields': ('permits',)
#         # }),
#         # ('Inspections', {
#         #     'classes': ('collapse',),
#         #     'fields': ('inspections',)
#         # }),
#     )
#
#
#
# # admin.site.register(Project, projectView)
# admin.site.register(Project_managers, pmView)
# admin.site.register(Resident_managers, rmView)
# admin.site.register(Design_package, deign_packageView)
# admin.site.register(General_contractor, general_contractorView)
# admin.site.register(Permit, permitView)
# admin.site.register(Inspection, inspectionView)
# admin.site.register(Inspection_type, inspection_typeView)
