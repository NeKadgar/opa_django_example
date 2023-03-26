from rest_framework import serializers
from apps.company.models import Company


class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)
