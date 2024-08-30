from django.views import View
from django.shortcuts import render
from . import models
from .forms import OrderForm


def index(request):
    return render(request, 'shop/index.html')


def list_bikes(request):
    bikes = models.Bike.objects.all
    return render(request, 'shop/bikes.html', {'bikes': bikes})


class OrderView(View):
    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs['pk']
        order = models.Order.objects.filter(id=pk).first()
        return render(request, 'shop/order.html', {'order': order})


class BikeView(View):
    def get(self, request, pk, *args, **kwargs):
        id = self.kwargs['pk']
        available = True
        bike = models.Bike.objects.filter(id=pk).first()
        frame = models.Frame.objects.filter(id=bike.frame.id).first()
        tire = models.Tire.objects.filter(id=bike.tire.id).first()
        seat = models.Seat.objects.filter(id=bike.seat.id).first()
        baskets = models.Basket.objects.first()
        if bike.has_basket and baskets.quantity < 1:
            available = False
        if frame.quantity < 1 or seat.quantity < 1 or tire.quantity < 2:
            available = False
        order_form = OrderForm()
        return render(request, 'shop/bike.html', {'bike': bike, 'available': available, 'order_form': order_form})

    def post(self, request, pk, *args, **kwargs):
        id = self.kwargs['pk']
        bike = models.Bike.objects.filter(id=pk).first()
        form = OrderForm(request.POST)
        order = form.save(commit=False)
        order.bike = models.Bike.objects.filter(id=pk).first()
        order.save()
        order.new_order()
        return render(request, 'shop/order.html', {'order': order})

