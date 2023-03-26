from django.db import models
from apps.company.models import Company


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
