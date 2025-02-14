from rest_framework.serializers import ModelSerializer
from ..models.Especie import Especie

class EspecieSerializer(ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'