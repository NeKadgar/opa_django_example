from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.company.models import Company, Team
from utils.subscription_consts import SUBSCRIPTIONS


class Subscription(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        choices=((name, name) for name in SUBSCRIPTIONS)
    )


class User(AbstractUser):
    is_organisation_admin = models.BooleanField(default=False)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField(Subscription, blank=True, related_name="users")

    @property
    def role(self):
        if self.is_superuser:
            return "admin"
        if self.is_staff:
            return "stuff"
        if self.is_organisation_admin:
            return "organisation_admin"
        return "employee"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                        ~models.Q(is_staff=True)
                        & ~models.Q(is_superuser=True)
                        | models.Q(company__isnull=True)
                        & models.Q(team__isnull=True)
                ),
                name='staff_and_superuser_have_no_company_or_team'
            ),
            models.CheckConstraint(
                check=(
                        models.Q(is_staff=True)
                        | models.Q(is_superuser=True)
                        | models.Q(company__isnull=False)
                        & models.Q(team__isnull=False)
                ),
                name='non_staff_and_non_superuser_have_company_and_team'
            ),
        ]
