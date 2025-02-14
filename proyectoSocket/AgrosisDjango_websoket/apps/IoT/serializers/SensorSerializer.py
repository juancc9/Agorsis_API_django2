from ..models.Sensor import Sensor
from rest_framework.serializers import ModelSerializer

class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'