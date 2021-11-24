from .models import List, Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'done']

class ListSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ['name', 'owner', 'url', 'item_set']