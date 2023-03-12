from .models import Portfolio_Item
from rest_framework import serializers

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio_Item
        fields = ['id', 'img', 'title', 'tech', 'desc', 'website']