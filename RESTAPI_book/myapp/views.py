from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics 
# Create your views here.

class BookList(generics.ListCreateAPIView):
	queryset=Book.objects.all()
	serializer_class=BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	lookup_field='isbn'
	queryset=Book
	serializer_class=BookSerializer

