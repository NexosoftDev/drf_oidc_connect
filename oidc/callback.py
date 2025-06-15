from mozilla_django_oidc.views import OIDCAuthenticationCallbackView
from django.shortcuts import redirect
from django.core.cache import cache


class CustomOIDCCallbackView(OIDCAuthenticationCallbackView):

    def get(self, request):
        response = super().get(request)

        access_token = request.session.get('oidc_access_token')

        if access_token and request.user.is_authenticated:

            cache_key = f"oidc_token_{request.user.email}"
            cache.set(cache_key, access_token, timeout=3600)

            return redirect('http://localhost:3000/')
        else:
            print("No encontré token en sesión o el usuario no está autenticado")
            return response
