from rest_framework import routers

from companies.views import CompanyViewSet

# Django Rest Framework provides a set of routers to handle URL routing for viewsets without having to manually define each URL pattern. Something like the following:

    # urlpatterns = [
    #     # List companies or create a new one
    #     path('companies/', CompanyViewSet.as_view({
    #         'get': 'list',
    #         'post': 'create'
    #     }), name='company-list-create'),

    #     # Retrieve, update, or delete a specific company
    #     path('companies/<int:pk>/', CompanyViewSet.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'patch': 'partial_update',
    #         'delete': 'destroy'
    #     }), name='company-detail'),
    # ]

# After setting up this router, you'll get a set of URL patterns that correspond to all the standard CRUD (Create, Retrieve, Update, Delete) operations provided by the CompanyViewSet.

companies_router = routers.DefaultRouter()
# The DefaultRouter class automatically generates URL patterns for your viewsets and also creates a default API root view, where you get a list of all registered API routes.

companies_router.register("companies", viewset=CompanyViewSet, basename="companies")
# With the register method, you're telling the router to handle URL generation for the CompanyViewSet.
# The first argument ("companies") is the URL prefix for this viewset. So, your API endpoint for companies might look something like: http://yourdomain.com/api/companies/.