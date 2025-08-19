from rest_framework import routers
from .viewsets import LibrosRestApiViewSet

router = routers.SimpleRouter()
router.register('librosrestapi', LibrosRestApiViewSet)

urlpatterns = router.urls
