from rest_framework import serializers
from .models import SupplierDetails, Sector

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class SupplierDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierDetails
        fields = '__all__'
