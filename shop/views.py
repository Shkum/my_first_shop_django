from datetime import datetime

from django.shortcuts import render

from .forms import SubscriberForm


def index(request):
    a = 'TEST'
    today = datetime.now().date().strftime('%A, %d %b %Y')
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        s = request.POST
        print(s)
        print(f"{s['name']} - {s.get('email')}")
        print(form.cleaned_data)
        new_form = form.save()

    return render(request, 'shop/index.html', locals())

