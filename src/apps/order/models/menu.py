from django.db import models

from src.apps.common.models import BaseModel
from src.apps.order.models.restaurant import Restaurant

class FoodItem(BaseModel):
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu')
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='food', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Food item'
        verbose_name_plural = 'Food items'
        ordering = ['-created_at']


