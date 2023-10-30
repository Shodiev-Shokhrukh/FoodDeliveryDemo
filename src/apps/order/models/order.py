from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point


from src.apps.account.models import User
from src.apps.common.models import BaseModel
from src.apps.order.models.menu import FoodItem
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
    order_location = gis_models.PointField(blank=True, null=True)
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
    def set_order_location(self, latitude, longitude):
        self.order_location = gis_models.Point(longitude, latitude)

    @property
    def total(self):
        return sum(item.food_item.price * item.quantity for item in self.order_items.all())
    
    @property
    def estimated_delivery_time(self):
        my_restaurant_location = gis_models.PointField(default=Point(41.3376534, 68.0660273))
        pending_accepted_orders = Order.objects.filter(status__in=['pending', 'accepted'])  # Get pending and accepted orders
        total_items = sum(sum(item.quantity for item in order.order_items.all()) for order in pending_accepted_orders)
        distance = calculate_distance(my_restaurant_location.location, self.order_location)        
        preparation_time = (total_items / 4) * 5
        delivery_time = distance * 3
        total_time = preparation_time + delivery_time

        return total_time
    
