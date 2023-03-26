from django.urls import path
from apps.company.views import create_company



urlpatterns = [
    path('create/', create_company),
]
