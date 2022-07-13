from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):

    brands = Car_brand.objects.all()

    my_data = {
        'brands':brands
    }


    return render(request, 'index.html')

@csrf_exempt
def add_brand(request):
    
    if request.method == 'POST':
        body = json.loads(request.body)
        brand_name = body['brandName']
        brand_details = body['brandDetails']
        hello = body['extra_info']
        print(brand_name)

        brand = Car_brand(name = brand_name, details = brand_details)
        brand.save()

        return JsonResponse(body)
    else:
         return render(request, 'add_brand.html') #HttpResponse 

def view_brand(request, id):

    selected_cars = Car.objects.all().filter(brand_id = id)
    brand = Car_brand.objects.get(id = id)

    my_data = {
        'selected_cars': selected_cars,
        'brand': brand.name
    }
    
    return render(request, 'view_brand.html', my_data)

@csrf_exempt
def edit_brand(request, id):

    if request.method == 'POST':
        body = json.loads(request.body)
        new_details = body['details']

        selected_brand = Car_brand.objects.get(id = id) # Searches for the car brand, and then gets changed on lines 59 & 60

        selected_brand.details = new_details
        selected_brand.save()

        return JsonResponse(body)
    else:

        brand = Car_brand.objects.get(id = id) # Allows us to grab the name

        my_data = {
            'id': id,
            'brand': brand.name
        }
        
        return render(request, 'edit_brand.html', my_data)


    


    





    
    

    

   
    
