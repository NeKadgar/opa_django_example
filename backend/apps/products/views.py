from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.models import Book
from utils.opa import opa_authorization


@api_view(['POST'])
@opa_authorization(Book.__class__.__name__)
def get_book(request):
    return Response({
        "message": f"Cool, you can access {Book.__class__.__name__} #{request.data.get('instance_id')}"
    })
