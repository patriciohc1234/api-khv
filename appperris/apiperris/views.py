from .models import Perro
from .serializers import PerroSerializer
from rest_framework import viewsets

class PerroViewSet(viewsets.ModelViewSet):
 
    serializer_class = PerroSerializer
    queryset = Perro.objects.all()

