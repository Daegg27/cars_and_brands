from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    brands = Car_brand.objects.all()

    my_data = {
        'brands':brands
    }


    return render(request, 'index.html', my_data)


def add_brand(request):
    
    return render(request, 'add_brand.html')
