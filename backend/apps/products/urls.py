from django.urls import path

from apps.products import views


urlpatterns = [
    path("book/", views.get_book)
]
