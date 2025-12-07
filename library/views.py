from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):

        qs = Book.objects.all()
        author = self.request.query_params.get("author")
        year = self.request.query_params.get("year")

        if author:
            qs = qs.filter(author__icontains=author)

        if year:
            qs = qs.filter(published_year=year)

        return qs


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def book_summary(request, pk):

    book = get_object_or_404(Book, pk=pk)
    data = {
        "id": book.id,
        "title": book.title,
        "short_summary": book.summary[:100], 
    }
    return Response(data)
