from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from oidc.callback import CustomOIDCCallbackView
from mozilla_django_oidc.views import OIDCAuthenticationRequestView

urlpatterns = [
    path('dadmin/', admin.site.urls),
    path('rest/v1/', include('apirest.urls', namespace='apirest')),
    path('rest/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('oidc/authenticate/', OIDCAuthenticationRequestView.as_view(), name='oidc_authentication_init'),
    path('oidc/callback/', CustomOIDCCallbackView.as_view(), name='oidc_authentication_callback'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)