from rest_framework import serializers
from .models import Treasury_Yield
class TreasuryYieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasury_Yield
        fields = ('bondName', 'couponRate', 'bondPrice', 'bondYield')