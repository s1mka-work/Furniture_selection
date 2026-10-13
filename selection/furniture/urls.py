from django.urls import path
from .views import OrderCreate, OrderResult

urlpatterns = [
    path('order/', OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/result/', OrderResult.as_view(), name='order_result'),
]