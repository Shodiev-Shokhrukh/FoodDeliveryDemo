from rest_framework import viewsets, permissions
from ..models.order import Order
from ..serializers.order import OrderSerializer
from src.apps.account.permissions import IsWaiter

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]  # Allow only authenticated users to create orders
        elif self.action in ['update', 'partial_update']:
            return [permissions.IsAuthenticated(), IsWaiter()]  # Waiters can update orders
        else:
            return [permissions.IsAuthenticated()]  # All authenticated users can view orders

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


    def perform_update(self, serializer):
        user = self.request.user
        instance = serializer.instance

        if user.role == 'waiter' and instance.status != 'accepted':
            instance.status = 'accepted'  # Logic for waiter accepting/sending orders
            instance.save()
        else:
            serializer.save()
