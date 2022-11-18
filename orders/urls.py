from django.contrib import admin
from django.urls import path

from orders import views

urlpatterns = [
    path('orders', views.orders, name='orders'),
]
