from django.shortcuts import render
from rest_framework import generics
from .models import GeneBank
from rest_framework import viewsets
from .serializers import GeneBankSerializer
# Create your views here.

class CustomGeneBankCreateView(generics.CreateAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer

class CustomGeneBankListView(generics.ListAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer

class GeneBankViewSet(viewsets.ModelViewSet):
    serializer_class = GeneBankSerializer
    queryset = GeneBank.objects.all()