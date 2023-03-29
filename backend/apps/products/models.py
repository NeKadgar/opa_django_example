from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.company.models import AbstractCompanyModel


class Footwear(AbstractCompanyModel):
    name = models.CharField(max_length=255)
    size = models.PositiveIntegerField(validators=[MaxValueValidator(50), MinValueValidator(25)])
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Book(AbstractCompanyModel, models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
