from django.contrib import admin
from django.forms import inlineformset_factory
from django.urls import path, include
import products.views
urlpatterns = [
    path('', products.views.productsHome, name='products'),
    path('second/', products.views.productsSecond),
]