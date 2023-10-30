from rest_framework import serializers

from src.apps.order.models.order import Order, OrderItem
 
from src.apps.order.serializers.menu import FoodSerializer
from src.apps.account.serializers.account import UserSerializer

class OrderItemSerializer(serializers.ModelSerializer):

    food_item = FoodSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'food_item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    
    order_items = OrderItemSerializer(many=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_items', 'user', 'distance', 'estimated_delivery_time', 'status', 'total']
        read_only_fields = ['id', 'user', 'estimated_delivery_time', 'status', 'total']

  