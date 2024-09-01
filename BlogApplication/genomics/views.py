from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):

    #This is a collection of objects from the db and can have filters
    queryset = Book.objects.all()
    # serializer to serialize and de-serialize the queryset objects
    serializer_class = BookSerializer