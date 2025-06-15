# perfiles/backends.py
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):

    def create_user(self, claims):
        """Crear usuario basado en los claims de OIDC"""
        email = claims.get('email')
        if not email:
            return None

        # Generar username desde el email si no existe
        username = email.split('@')[0]

        # Extraer otros campos que necesites del claim
        user_data = {
            'username': username,
            'first_name': claims.get('given_name', ''),
            'last_name': claims.get('family_name', ''),
            'is_active': True,
        }

        # Remover campos None o vacíos
        user_data = {k: v for k, v in user_data.items() if v is not None}

        # Llamar al manager con email como argumento separado
        user = User.objects.create_user(email=email, **user_data)
        return user

    def update_user(self, user, claims):
        """Actualizar usuario existente con nuevos claims"""
        user.first_name = claims.get('given_name', user.first_name)
        user.last_name = claims.get('family_name', user.last_name)
        user.email = claims.get('email', user.email)
        user.save()
        return user

    def filter_users_by_claims(self, claims):
        """Filtrar usuarios por email"""
        email = claims.get('email')
        if not email:
            return self.UserModel.objects.none()
        return self.UserModel.objects.filter(email__iexact=email)