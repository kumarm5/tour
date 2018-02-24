from rest_framework.viewsets import ModelViewSet
from .serializers import SectorSerializer, SupplierDetailsSerializer
from .models import Sector, SupplierDetails

class SectorViewSet(ModelViewSet):
    queryset = Sector.objects.filter(status=True)
    serializer_class = SectorSerializer
    
class SupplierDetailsViewSet(ModelViewSet):
    queryset = SupplierDetails.objects.all()
    serializer_class = SupplierDetailsSerializer
