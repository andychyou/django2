import re
from django.shortcuts import render

# Create your views here.


def first(request):
    return render(request, 'myapp/first.html')

def second(request):
    return render(request, 'myapp/second.html')

