from django import forms
from .models import OrderItem, Order
from django.forms import inlineformset_factory

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['manufacturer', 'system', 'type', 'width', 'height', 'count', 'additional']

OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderForm, extra=1)