from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Item 
import math
from .models import Customer, Service

def index(request):
    name = request.user.username
    return render(request, "index.html", {'name':name})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('registration')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def map(request):
    return render(request, 'map.html')

     
def pickup(request):
    item_list = Item.objects.all()
    items = {}
    count = 0
    return render(request,'pickup.html',{'item_list':item_list})

def itemForm(request):
    itemType = str(request.POST.get('type'))
    user = request.user.username
    item_list = Item.objects.all().filter(itemType=itemType)
    
    itemCount = {}
    for key in item_list:
        itemCount[key.itemName] = request.POST.get(key.itemName) 
        print(key.itemName, request.POST.get(key.itemName))

    customer  = Customer.objects.filter(name=user)
    # logic
    shopName = ""
    slot = 1
    validShops =  Service.objects.filter(shopType = itemType).filter(zoneID=customer[0].zoneID).filter(numCust__lt=3).order_by('slotID')
    if(len(validShops) == 0):
        slot = "Try again later"
        shopName="No shops found"
        return render(request, 'output.html', {'name':user, 'shop_name':shopName, 'slot_time':slot, 'itemCount': itemCount})
    dist = math.inf
    for shop in validShops:
        d = math.sqrt((customer[0].lon - shop.lon)**2 + (customer[0].lan - shop.lan)**2)
        if(dist < d):
            dist = d
            shopName = shop.name
            slot = shop.slotID
    selectedshop = Service.objects.filter(name=shopName).filter(slot=slot)
    selectedshop.numCust = selectedshop.numCust + 1
    return render(request, 'output.html', {'name':user, 'shop_name':shopName, 'slot_time':slot, 'itemCount': itemCount})

def delivery(request):
    item_list = Item.objects.all()
    items = {}
    count = 0
    return render(request,'delivery.html',{'item_list':item_list})


# def manager(request):


# def shop(request):
#     # pickup/ delivery

# def pickup():
    
#     # select items to be bought
#     # implement logic to find optimal shop and add to queue
#     # this should finally return shop name and location and time

# def delivery():
#     # select Amazon/Flipkart/Retailer
#     # return shop from which delivery will happen

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                pass
                #messages.error(request, "Invalid username or password.")
        else:
            pass
            #messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})

def registerCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomerForm()
    return render(request, 'registration.html',{'form':form})


def fruits_and_veg(request):
    item_list = Item.objects.all().filter(itemType='Fruits')
    return render(request, 'fruitsVeg.html',{'item_list':item_list})

def dairy(request):
    item_list = Item.objects.all().filter(itemType='Dairy')
    return render(request, 'dairy.html',{'item_list':item_list})

def medicine(request):
    item_list = Item.objects.all().filter(itemType='Medicine')
    return render(request, 'medicine.html',{'item_list':item_list})

def cereals_and_pulses(request):
    item_list = Item.objects.all().filter(itemType='Cereals')
    return render(request, 'cereals.html',{'item_list':item_list})
