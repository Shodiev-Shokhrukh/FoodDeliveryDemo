from django.contrib.gis.geos import fromstr

from rest_framework import serializers

from src.apps.order.models.restaurant import Restaurant

class LocationField(serializers.Field):

    def to_representation(self, value):
        return (f"{value.x}, {value.y}")

    def to_internal_value(self, data):
        latitude, longitude = data.split(',')
        try:
            return fromstr(f'POINT({longitude} {latitude})')
        except:
            raise serializers.ValidationError('Invalid location')

class RestaurantSerializer(serializers.ModelSerializer):

    location = LocationField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'location', 'opening_hours', 'closing_hours', 'image',)
        
        read_only_fields = ['id', 'created_at', 'updated_at']