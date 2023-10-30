from django.contrib import admin
from django.contrib.gis import forms

from src.apps.order.models.menu import FoodItem 
from src.apps.order.models.order import Order, OrderItem
from src.apps.order.models.restaurant import Restaurant

class AdminForm(forms.ModelForm):
    location = forms.PointField(widget=forms.OSMWidget(attrs={
        'display_raw': 'true',
    }), required=False)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "opening_hours", "closing_hours", "image",)
    search_fields = ("name",)
    list_filter = ("opening_hours", "closing_hours",)
    list_display_links = ("id", "name",)
    form = AdminForm


@admin.register(FoodItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "image",)
    search_fields = ("title",)
    list_filter = ("price",)
    list_display_links = ("id", "title",)
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'food_item', 'quantity']
    # Customize further as needed

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status']
    inlines = [OrderItemInline]
    readonly_fields = ['status']
    form  = AdminForm