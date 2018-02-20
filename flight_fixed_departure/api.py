from rest_framework.viewsets import ModelViewSet
from .serializers import SectorSerializer
from .models import Sector

class SectorViewSet(ModelViewSet):
    queryset = Sector.objects.filter(status=True)
    serializer_class = SectorSerializer
    