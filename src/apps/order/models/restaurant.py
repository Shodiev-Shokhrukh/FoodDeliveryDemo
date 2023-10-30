from src.apps.common.models import BaseModel

from django.contrib.gis.db.models import PointField
from django.db import models

class Restaurant(BaseModel):

    name = models.CharField('Name of Restaurant', max_length=255, blank=False, null=False)
    location = PointField('Location of a restaurant', blank=True, null=True)
    opening_hours = models.TimeField('Opening Hours', blank=True, null=True)
    closing_hours = models.TimeField('Closing Hours', blank=True, null=True)
    image = models.ImageField('Image of Restaurant', upload_to='restaurant/', blank=True, null=True)

    class Meta:

        ordering = ['id']
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
    
    def __str__(self):
        return self.name
    