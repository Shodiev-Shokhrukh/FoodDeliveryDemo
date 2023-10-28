from rest_framework import serializers

from ..models.menu import FoodItem

class FoodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields = ('id', 'title', 'description', 'price', 'image')
        read_only_fields = ('id',)
        extra_kwargs = {
            'image': {'required': False}
        }

