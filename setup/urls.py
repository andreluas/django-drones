from django.contrib import admin
from django.urls import path, include
from demanda.views import DemandaViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="VeeCode - Demandas API",
      default_version='v1.0',
      description="API de Demandas - Desafio Finxi",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@finxi.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('demanda', DemandaViewSet, basename='demandas')

urlpatterns = [
    path('controle-geral/', admin.site.urls),
    path('', include(router.urls) ),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
