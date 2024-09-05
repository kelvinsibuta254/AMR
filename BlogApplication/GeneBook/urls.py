from rest_framework.routers import DefaultRouter
from .views import GeneBankViewSet

router = DefaultRouter()
"""router returns a list of urlpatterns"""

router.register("GeneBook", GeneBankViewSet, basename="GeneBook")

urlpatterns = router.urls