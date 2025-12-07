from django.urls import path
from .views import BookListCreateView, BookDetailView, book_summary

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/summary/", book_summary, name="book-summary"),
]
