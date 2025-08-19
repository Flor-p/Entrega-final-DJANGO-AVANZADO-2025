from rest_framework import viewsets
from .models import LibrosResApi
from .serializer import LibrosRestApiSerializer

class LibrosRestApiViewSet(viewsets.ModelViewSet):
    queryset = LibrosResApi.objects.all()
    serializer_class = LibrosRestApiSerializer
