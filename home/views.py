from django.shortcuts import render
from products.models import Product
import random


def homepage(request):
    products = list(Product.objects.all())

    products = random.sample(products, 4)

    return render(request, 'home/index.html', {'products': products})
