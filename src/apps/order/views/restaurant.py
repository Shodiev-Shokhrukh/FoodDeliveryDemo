from django.shortcuts import get_object_or_404

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.order.models.menu import FoodItem
from src.apps.order.models.restaurant import Restaurant
from src.apps.order.serializers.menu import FoodSerializer
from src.apps.order.serializers.restaurant import RestaurantSerializer
from src.apps.account.permissions import IsWaiterOrAdmin

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsWaiterOrAdmin]

    def check_permission(self):
        user = self.request.user
        return user.role in ['waiter', 'admin']

    def perform_action(self, action, serializer):
        if self.check_permission():
            print(f"Waiter or admin is {action} the restaurant")
            serializer.save()

    def perform_update(self, serializer):
        self.perform_action("updating", serializer)

    def perform_create(self, serializer):
        self.perform_action("creating", serializer)

    def perform_destroy(self, instance):
        if self.check_permission():
            print("Waiter or admin is deleting the restaurant")
            instance.delete()

class RestaurantMenu(APIView):

    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        food_items = FoodItem.objects.filter(restaurant=restaurant)
        return Response(
            {
                "restaurant": RestaurantSerializer(restaurant).data, 
                "menu": [FoodSerializer(i).data for i in food_items]
                }
            )
