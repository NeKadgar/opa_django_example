from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from apps.users.models import User
from apps.company.models import Team
from utils.opa import set_opa_data


@receiver(pre_save, sender=User)
def add_default_team(sender, instance: User, **kwargs):
    if instance.is_superuser or instance.is_staff:
        return

    if instance.team is None:
        default_team = Team.objects.filter(company_id=instance.company.pk, is_default=True).first()
        instance.team = default_team


# @receiver(post_save, sender=User)
# def update_opa_user(sender, instance: User, created, **kwargs):
#     user_data = dict()
#     if instance.is_superuser or instance.is_staff:
#         user_data["role"] = "admin" if instance.is_superuser else "stuff"
#     else:
#         user_data.update({
#             "role": "organisation_admin" if instance.is_organisation_admin else "employee",
#             "company_id": instance.company.pk,
#             "team_id": instance.team.pk
#         })
#     set_opa_data(f"users/{instance.pk}", user_data)
