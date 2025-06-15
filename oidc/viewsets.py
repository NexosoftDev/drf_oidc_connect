from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import User
from oidc.serializers import UserSerializer

# Create your views here.

class OidcViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[AllowAny], url_path='get-token', url_name='get-token')
    def get_token(self, request):
        """
        Endpoint para obtener el token OIDC de la sesión actual.
        No requiere autenticación ya que usa la sesión de Django.
        """
        token = request.session.get('oidc_access_token')

        if token:
            return Response({
                'access_token': token
            })
        return Response({
            'error': 'No token found in session'
        }, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'], url_path='me', url_name='me')
    def me(self, request):
        """
        Endpoint para obtener los datos del usuario actual.
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
