from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.models import Book
from apps.products.serializers import BookSerializer
from utils.opa import opa_authorization


@api_view(['POST'])
@opa_authorization(Book.__class__.__name__)
def get_book(request):
    return Response({
        "message": f"Cool, you can access {Book.__class__.__name__} #{request.data.get('instance_id')}"
    })


@api_view(['GET'])
def get_available_books(request):
    if request.user.is_superuser or request.user.is_staff:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(company=request.user.company)
        if not request.user.is_organisation_admin:
            books = books.filter(Q(access_tags__in=request.user.team.access_tags.all()) | Q(access_tags=None))
    return Response(BookSerializer(books, many=True).data)
