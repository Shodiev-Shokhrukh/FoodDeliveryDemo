from rest_framework import permissions
from rest_framework import viewsets
from ..models.menu import FoodItem
from ..serializers.menu import FoodSerializer
from src.apps.account.permissions import IsWaiterOrAdmin

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsWaiterOrAdmin]

    def check_permission(self):
        user = self.request.user
        return user.role in ['waiter', 'admin']

    def perform_action(self, action, serializer):
        if self.check_permission():
            print(f"Waiter or admin is {action} the food")
            serializer.save()

    def perform_update(self, serializer):
        self.perform_action("updating", serializer)

    def perform_create(self, serializer):
        self.perform_action("creating", serializer)

    def perform_destroy(self, instance):
        if self.check_permission():
            print("Waiter or admin is deleting the food")
            instance.delete()
