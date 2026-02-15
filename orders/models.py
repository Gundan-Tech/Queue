from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    # Status choices for the tracking system
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    logo_reference = models.CharField(max_length=255, blank=True, null=True, help_text="Text or image path for CNC")
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def remaining_balance(self):
        return self.total_price - self.paid_balance

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255) 
    size = models.CharField(max_length=100)      
    quantity = models.PositiveIntegerField(default=1)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    item_photo = models.ImageField(upload_to='item_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} x {self.item_name}"
