from ..models.Tipo_Sensor import Tipo_Sensor
from rest_framework.serializers import ModelSerializer

class Tipo_SensorSerializer(ModelSerializer):
    class Meta:
        model = Tipo_Sensor
        fields = '__all__'