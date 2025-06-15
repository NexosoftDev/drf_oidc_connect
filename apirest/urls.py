from django.urls import include, path
from rest_framework import routers
from users.viewsets import RegisterViewSet, AuthTokenViewset, LogoutViewset, TokenRefreshViewSet, UserViewSet
from dynamic_preferences.api.viewsets import GlobalPreferencesViewSet

drf_router = routers.DefaultRouter()

drf_router.register(r'user/auth/register', RegisterViewSet, basename="register")
drf_router.register(r'user/auth/login', AuthTokenViewset, basename="auth-token")
drf_router.register(r'user/auth/logout', LogoutViewset, basename="logout")
drf_router.register(r'user/auth/refresh-token', TokenRefreshViewSet, basename="refresh-token")

drf_router.register(r'config/global/dynamics', GlobalPreferencesViewSet, basename="global-config")


app_name = 'apirest'

urlpatterns = [

    path('', include(drf_router.urls)),
    path('catalogo/', include('catalogo.urls')),
    path('oidc/', include('oidc.urls')),


]

urlpatterns += drf_router.urls