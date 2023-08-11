from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from companies.models import Company
from companies.serializers import CompanySerializer

class CompanyViewSet(ModelViewSet):
    # A ModelViewSet is a type of viewset that provides default CRUD (Create, Retrieve, Update, Delete) operations for a model.

    serializer_class = CompanySerializer
    # This specifies that the viewset should use the CompanySerializer to serialize and deserialize instances of the Company model.

    queryset = Company.objects.all().order_by("-last_update")
    # In Django, every model class has at least one manager, and the default name for this manager is objects. Managers are used to create querysets.
    # .all() is a method on the manager that returns a queryset that represents all Company instances stored in the database.

    # Here are a few examples of what a queryset for Company instances might look like using Django's ORM.
    # all_companies = Company.objects.all()
    # specific_company = Company.objects.get(id=5)
    # active_company_count = Company.objects.filter(status="Active").count()

    pagination_class = PageNumberPagination
    # Using PageNumberPagination means that results will be split into "pages" of a certain size, and each request will return just one of those pages.
    # This helps in scenarios where there are many Company records and returning all of them in a single API response would be inefficient or slow.

