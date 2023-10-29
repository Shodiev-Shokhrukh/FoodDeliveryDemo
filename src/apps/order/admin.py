from django.contrib import admin

from src.apps.order.models.menu import FoodItem 
from src.apps.order.models.order import Order

@admin.register(FoodItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "image",)
    search_fields = ("title",)
    list_filter = ("price",)
    list_display_links = ("id", "title",)
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","distance", 'status')
    search_fields = ("id", )