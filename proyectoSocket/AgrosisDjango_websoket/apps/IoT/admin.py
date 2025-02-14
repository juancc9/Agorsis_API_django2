from django.contrib import admin

from .models.Sensor import Sensor
from .models.Configuracion import Configuracion
from .models.Tipo_Sensor import Tipo_Sensor

# Register your models here.

admin.site.register(Sensor)
admin.site.register(Configuracion)
admin.site.register(Tipo_Sensor)