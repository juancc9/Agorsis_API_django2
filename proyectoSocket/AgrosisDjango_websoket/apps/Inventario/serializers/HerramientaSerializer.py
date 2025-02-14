from rest_framework.serializers import ModelSerializer
from ..models.Herramienta import Herramienta

class HerramientaSerializer(ModelSerializer):
    class Meta:
        model = Herramienta
        fields = '__all__'