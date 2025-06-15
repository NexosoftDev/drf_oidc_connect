from rest_framework import viewsets, permissions
from catalogo.serializers import ArregloFloralSerializer
from catalogo.models import ArregloFloral


class ArregloFloralViewSet(viewsets.ModelViewSet):
    queryset = ArregloFloral.objects.all()
    serializer_class = ArregloFloralSerializer
    permission_classes = [permissions.IsAuthenticated]
