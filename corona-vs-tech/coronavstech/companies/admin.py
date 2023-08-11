from django.contrib import admin

from companies.models import Company

@admin.register(Company)
# A decorator provided by Django. You can now view, add, change, and delete instances of the Company model via the Django admin interface.
class CompanyAdmin(admin.ModelAdmin):
    #  This defines a new admin class for the Company model. By subclassing the admin.ModelAdmin class, you can customize and extend how the Company model behaves and is displayed in the admin interface. For instance:
    # CRUD Operations
    # Determine which fields of the model are displayed in the changelist.
    # Allow certain fields to be editable directly from the changelist.
    # Add filters to the right sidebar of the changelist page allowing filtering of displayed results.
    # Add a search bar
    pass