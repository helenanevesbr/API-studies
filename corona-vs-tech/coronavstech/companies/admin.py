from django.contrib import admin

from companies.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass