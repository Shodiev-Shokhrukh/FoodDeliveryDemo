from django.db import models
from django.utils import timezone

from src.apps.account.models import User
from src.apps.order.models.menu import FoodItem



class Order(models.Model):
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('delivered', 'Delivered'),
    ]
    
    items = models.ManyToManyField(FoodItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    distance = models.FloatField(null=True, blank=True, default=5)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    class Meta:
        ordering = ['id']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'Order #{self.id}'
    
    @property
    def total(self):
        return sum(item.price for item in self.items.all())
    
    @property
    def estimated_delivery_time(self):
        items_count = self.items.count()  
        delivery_distance = self.distance  

        preparation_time = (items_count / 4) * 5  


        delivery_time = delivery_distance * 3  

        total_time = preparation_time + delivery_time

        return total_time
    
