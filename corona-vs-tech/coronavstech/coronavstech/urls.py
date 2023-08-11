"""
URL configuration for coronavstech project.
The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

from companies.urls import companies_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(companies_router.urls)),
]
