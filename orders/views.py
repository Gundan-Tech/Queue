
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order


# This is the view for your main queue list (The one causing the error)
class DashboardView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/dashboard.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

# This is the view for looking at specific CNC specs/logos
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetching all items related to this specific order
        context['items'] = self.object.items.all()
        return context