from datetime import datetime

from django.shortcuts import render

def orders(request):
    return render(request, 'shop/index.html')



