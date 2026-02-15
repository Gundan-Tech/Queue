from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'delivery_date', 'status', 'total_price', 'remaining_balance')
    list_filter = ('status', 'delivery_date')
    search_fields = ('customer_name', 'customer_phone')
    inlines = [OrderItemInline]