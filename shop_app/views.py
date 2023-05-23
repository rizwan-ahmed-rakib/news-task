from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here for your models
from shop_app.models import Product, Category

"""classbase view"""


class Home(ListView):
    model = Product
    template_name = 'shop_app/home.html'
