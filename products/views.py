from datetime import datetime

from django.shortcuts import render


def products(request):
    return render(request, 'shop/index.html')