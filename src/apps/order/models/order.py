from django.db import models

from src.apps.account.models import User
from src.apps.order.models.menu import FoodItem

class Order(models.Model):
    food = models.ManyToManyField(FoodItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    distance = models.FloatField(null=True, blank=True, default=5)
    estimated_delivery_time = models.DateTimeField()
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('delivered', 'Delivered'),
    ]

    class Meta:
        ordering = ['id']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'Order #{self.id}'
    
    @property
    def status(self):
        return self.STATUS_CHOICES[self.status][1]
    
    @status.setter
    def status(self, status):
        self.status = self.STATUS_CHOICES.index(status)
        
    @property
    def total(self):
        return sum(self.food.price)
    