
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
@require_POST
def update_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    # Simple logic: Pending -> In Progress -> Completed
    if order.status == 'Pending':
        order.status = 'In Progress'
    elif order.status == 'In Progress':
        order.status = 'Completed'
    
    order.save()
    return redirect('dashboard')

    
class DashboardView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/dashboard.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        queryset = Order.objects.all().order_by('-created_at')
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()
        return context