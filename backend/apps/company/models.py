from django.db import models
from apps.users.models import MyUser


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
