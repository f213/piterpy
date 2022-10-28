from rest_framework.viewsets import ModelViewSet

from books.api.serializers import BookSerializer
from books.models import Book


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
