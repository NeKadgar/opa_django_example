from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.company.serializers import CreateCompanySerializer
from utils.opa import opa_authorization


@api_view(['POST'])
@opa_authorization(policy="1234")
def create_company(request):
    serializer = CreateCompanySerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({})
