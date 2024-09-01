from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.response import Response
from rest_framework import status
from .models import Gene
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import GeneSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class GeneListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GeneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer



# Create your views here.

class GeneViewSet2(viewsets.ViewSet):
    """
    Viewset --> is a class-based view which doesn't provide any method handlers
    for your request

    View --> is a python function or python class that accepts Http request and 
    returns and Http Response
    """
    
    def list(self, request):
        """This is a method instance:
        Returns a list of members"""
        genes = Gene.objects.all()

        #serialize and deserialize queryset
        serializer = GeneSerializer(genes, many=True)
        """many=True returns a list of members"""
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        gene = Gene.objects.filter(pk=pk).first()
        if not gene:
            message = {"detail": f"member with id {pk} is not found"}
        serializer = GeneSerializer(gene)
        return Response(serializer.data)
    
    def create(self, request):
        queryset = Gene.objects.create(**request.data)
        serializer = GeneSerializer(queryset)
        return Response(serializer.data)

    def update(self, request):
        pass

    def partial_update(self, request, pk):
        pass

    def destroy(self, request, pk):
        return Response(status=status.NO_CONTENT)

class GeneViewSet(viewsets.ModelViewSet):
    serializer_class = GeneSerializer
    queryset = Gene.objects.all()

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Only authenticated users can access this view"""
        return Response(
            {"message": "Hello authenticated user!"}
        )
    
class IsAdminOrReadOnly(BasePermission):
    """This is a custom permission class
    Allow read-only access to everyone, but requires the user to be admin (staff) for any write permissions"""
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return request.user.is_staff
    
class MyModelListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Only authenticated users can view the list of models"""
        queryset = Gene.objects.all()
        serializer = GeneSerializer(queryset, many=True)
        return Response(serializer.data)
    
class MyModelCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        """Only admin users can create new model instances"""
        serializer = GeneSerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)