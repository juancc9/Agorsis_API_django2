from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Usuario
from ..serializers.userSerializer import UsuarioSerializer

class UsuarioViews(ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class =UsuarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]