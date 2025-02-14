from rest_framework.routers import DefaultRouter
from ..views.HerramientaViews import HerramientaViews

HerramientaRouter = DefaultRouter()
HerramientaRouter.register(prefix='herramienta',viewset=HerramientaViews,basename='herramienta')