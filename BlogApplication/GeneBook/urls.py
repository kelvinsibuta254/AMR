from rest_framework.routers import DefaultRouter
from .views import GeneBankViewSet
from .views import GeneBankCreateView, GeneBankListView, GeneBankRetrieveView, CustomGeneBankCreateView, GeneBankList, CustomGeneBankListView, GeneBankViewSet, RetrieveGeneBankView, BaseRetrieveView, BaseRetrieveUpdateDestroyView
from django.urls import path
from .models import GeneBank
from .serializers import GeneBankSerializer

# router = DefaultRouter()
# """router returns a list of urlpatterns"""

# router.register("GeneBook", GeneBankViewSet, basename="GeneBook")

# urlpatterns = router.urls
urlpatterns = [
    path('genebank/create', GeneBankCreateView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='genebank-create'),
    path('gene/', CustomGeneBankCreateView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='create-list'),
    path('genebank/list', CustomGeneBankListView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='genebank-list'),
    path('genebanklist/', GeneBankListView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='genebanklist'),
    path('genebank/retrieve', RetrieveGeneBankView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='genebank-retrieve'),
    path('gene/retrieve', GeneBankRetrieveView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='gene-detail'),
    #path('gene/<int:pk>/', GeneBankRetrieveView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='gene-retrieve'),

    ]