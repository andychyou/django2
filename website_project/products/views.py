from django.shortcuts import render

# Create your views here.

def productsHome(request):
    return render(request, 'products/first.html')


def productsSecond(request):
    return render(request, 'products/second.html')