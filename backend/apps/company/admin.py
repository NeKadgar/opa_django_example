from django.contrib import admin
from apps.company.models import Company, Team, AccessTag


admin.site.register(Company)
admin.site.register(AccessTag)
admin.site.register(Team)
