from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .forms import OrderFormSet
from .models import Order
from .logic.calculator import engine, price_calculate, storage_output


class OrderCreate(View):
    template_name = 'make_order/order.html'

    def get(self, request):
        formset = OrderFormSet()
        return render(request, self.template_name, {'formset': formset})

    def post(self, request):
        formset = OrderFormSet(request.POST)

        if formset.is_valid():
            order = Order.objects.create()

            formset.instance = order
            formset.save()

            return redirect('order_result', pk=order.pk)
        return render(request, self.template_name, {'formset': formset})

class OrderResult(View):
    template_name = 'make_order/order_result.html'

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        result = []
        total_price = 0

        for item in order.items.all():
            furniture_result = engine(item)
            price = price_calculate(furniture_result)

            result.append({
                'item': item,
                'furniture': furniture_result,
                'price': price,
            })

            total_price += price

        return render(request, self.template_name, {
            'order': order,
            'result': result,
            'total_price': total_price,
        })

