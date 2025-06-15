from rest_framework.routers import DefaultRouter
from oidc.viewsets import OidcViewset

router = DefaultRouter()
router.register(r'obtener-token', OidcViewset, basename='obtener-token')

urlpatterns = router.urls