from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from apps.company.models import Team, Company, AbstractCompanyModel
from utils.opa import set_opa_data


@receiver(post_save, sender=Company)
def create_default_team(sender, instance: Company, created, **kwargs):
    Team(
        name="Default Team",
        is_default=True,
        company=instance
    ).save()


@receiver(m2m_changed)
def update_opa_access_tags(sender, instance, action: str, **kwargs):
    if not action.startswith('post_') or sender in [LogEntry, Session]:
        return

    if issubclass(instance.__class__, AbstractCompanyModel):
        tags = list(instance.access_tags.values_list("pk", flat=True))
        set_opa_data(f"company_entities/{instance.company.pk}/{instance.__class__.__name__}/{instance.pk}", tags)

    if isinstance(instance, Team):
        tags = list(instance.access_tags.values_list("pk", flat=True))
        set_opa_data(f"teams/{instance.pk}", tags)
