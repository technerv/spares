from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import CarDetails

# Create your views here.
@csrf_exempt
def index(request):
    itemstock = CarDetails.objects.all()
    return render(request, "spareapp/index.html", {"itemstock": itemstock})

@csrf_exempt
def add_item(request):
    if request.method == "POST":
        item_name = request.POST['item_name']
        car_make = request.POST['car_make']
        model_number = request.POST['model_number']
        price = request.POST['price']
        stock = CarDetails.objects.create(item_name=item_name, car_make=car_make, model_number=model_number, price=price)
        messages.info(request, "ITEM ADDED SUCCESSFULLY")
        return redirect('/')
    else:
        #messages.info(request, "PLEASE ADD A NEW ITEM")
        itemstock = CarDetails.objects.all()
        return render(request, "spareapp/index.html", {"itemstock": stock})

@csrf_exempt
def delete_item(request, pk):
    stock = CarDetails.objects.get(id=pk)
    stock.delete()
    messages.info(request, "ITEM SUCCESSFULLY DELETED")
    return redirect('spareapp:index')

@csrf_exempt
def edit_item(request, pk):
    itemselect = CarDetails.objects.get(id=pk)
    return render(request, "spareapp/index.html", {"itemselect":itemselect})

@csrf_exempt
def update_item(request, pk):
    item = CarDetails.objects.get(id=pk)
    item.item_name = request.POST['item_name']
    item.car_make = request.POST['car_make']
    item.model_number = request.POST['model_number']
    item.price = request.POST['price']
    item.save()
    messages.info(request, "ITEM UPDATED SUCCESSFULLY")
    return redirect('spareapp:index')
