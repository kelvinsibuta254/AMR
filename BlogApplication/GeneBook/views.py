from django.shortcuts import render
from rest_framework import generics, mixins
from .models import GeneBank
from rest_framework import viewsets
from .serializers import GeneBankSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.

class CustomGeneBankCreateView(generics.CreateAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer

# Overrides the view and set several classes
class GeneBankList(generics.ListCreateAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of 'get_queryset()' instead of 'self.queryset'
        queryset = self.get_queryset()
        serializer = GeneBankSerializer(queryset, many=True)
        return Response(serializer.data)

class GeneBankCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GeneBankListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer
# Used for get requests
    def get(self, request, *args, **kwargs): # args pass positional arguments to the view
        return self.list(request, *args, **kwargs)

class GeneBankRetrieveView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class CustomGeneBankListView(generics.ListAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer

class GeneBankViewSet(viewsets.ModelViewSet):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer

from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin):
    """Makes sure that people must login to access this view"""
    login_url = '/login/' # define a url someone is going to be redirected to when they are not logged in
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        """This is a get request for one item or list of items"""
        pass


from .mixins import MultipleFieldLookupMixin, AllowPUTAsCreateMixin

class RetrieveGeneBankView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer
    lookup_fields = '__all__'

class BaseRetrieveView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer
    lookup_fields = '__all__'

class BaseRetrieveUpdateDestroyView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneBank.objects.all()
    serializer_class = GeneBankSerializer
    lookup_fields = ['Gene', 'Region']