from rest_framework import serializers

from src.apps.order.models.order import Order
 
from src.apps.order.serializers.menu import FoodSerializer
from src.apps.account.serializers.account import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    
    items = FoodSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'items', 'user', 'distance', 'estimated_delivery_time', 'status', 'total']
        read_only_fields = ['id', 'user', 'estimated_delivery_time', 'status', 'total']

  