from django.db import models
from django.contrib.auth.models import AbstractUser


class EmployeeGroup(models.Model):
    name = models.CharField(max_length=255)


class EmployeeGroupPermission(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(EmployeeGroup, on_delete=models.CASCADE)

OWNER = 'owner'
EMPLOYEE = 'employee'
class MyUser(AbstractUser):

    ROLE_CHOICES = [
        (OWNER, OWNER),
        (EMPLOYEE, EMPLOYEE),
    ]

    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    group = models.OneToOneField(EmployeeGroup, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(role=OWNER) & models.Q(group__isnull=True) |
                      ~models.Q(role=OWNER),
                name='owner_group_check'
            )
        ]
