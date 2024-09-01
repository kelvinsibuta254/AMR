from django.urls import path
from .views import GeneListCreateAPIView, GeneRetrieveUpdateDestroyAPIView, GeneViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('genes/', GeneListCreateAPIView.as_view(), name='gene-list-create'),
    path('genes/<int:pk>/', GeneRetrieveUpdateDestroyAPIView.as_view(), name='gene-retrieve-update-destroy'),
]


router = DefaultRouter()
"""router returns a list of urlpatterns"""

router.register("bioinformatics", GeneViewSet, basename="bioinformatic")

urlpatterns = router.urls