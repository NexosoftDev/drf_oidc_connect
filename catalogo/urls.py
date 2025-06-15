from rest_framework.routers import DefaultRouter
from catalogo.viewsets import ArregloFloralViewSet

router = DefaultRouter()
router.register(r'obtener-catalagos', ArregloFloralViewSet, basename='catalogos')

urlpatterns = router.urls