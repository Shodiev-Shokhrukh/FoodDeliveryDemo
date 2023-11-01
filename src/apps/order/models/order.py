from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point


from src.apps.account.models import User
from src.apps.common.models import BaseModel
from src.apps.order.models.menu import FoodItem
from src.apps.order.models.restaurant import Restaurant
from src.apps.order.utils import calculate_distance


class OrderItem(BaseModel):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['id']
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
    
    def __str__(self):
        return f'Order #{self.order.id} Item #{self.id}'
    
class Order(BaseModel):
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('delivered', 'Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = gis_models.PointField(blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    class Meta:
        ordering = ['id']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'Order #{self.id}'
    
    @property
    def order_items(self):
        return OrderItem.objects.filter(order=self)

    @property
    def estimated_delivery_time(self):
        pending_accepted_orders = Order.objects.filter(status__in=['pending', 'accepted'])  # Get pending and accepted orders
        total_items = sum(sum(item.quantity for item in order.order_items.all()) for order in pending_accepted_orders)
        distance = calculate_distance(self.restaurant.location, self.location)        
        preparation_time = (total_items / 4) * 5
        delivery_time = distance * 3
        total_time = preparation_time + delivery_time

        return total_time
    
