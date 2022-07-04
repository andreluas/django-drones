from urllib import request
from rest_framework import viewsets
from demanda.models import Demanda
from demanda.serializer import DemandaSerializer
from demanda.permissions import IsUserOrUnauthenticated
from rest_framework.authentication import BasicAuthentication
    
class DemandaViewSet(viewsets.ModelViewSet):
    """Lista de demandas"""
    queryset = Demanda.objects.all()
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.queryset.filter(user=self.request.user)
        else:
            return Demanda.objects.all()
    serializer_class = DemandaSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    permission_classes = [IsUserOrUnauthenticated]
    authentication_classes = [BasicAuthentication]