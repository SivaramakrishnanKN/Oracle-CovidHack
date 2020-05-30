from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Item 
import math
from .models import Customer, Service, Item

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    name = request.user.username

    return render(request, "index.html", {'name':name})

def logout_view(request):
    logout(request)
    return redirect('index')

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
    if not request.user.is_authenticated:
        return redirect('/login')
    item_list = Item.objects.all()
    items = {}
    count = 0
    if request.session.get('coun') == 1:
        request.session['coun'] = 0
    else:
        request.session['site']=''
    return render(request,'pickup.html',{'item_list':item_list})

def itemForm(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    itemType = str(request.POST.get('type'))
    user = request.user.username
    item_list = Item.objects.all().filter(itemType=itemType)

    site = request.session.get('site')
  
    total = 0.0

    itemCount = {}
    for key in item_list:
        itemCount[key.itemName] = request.POST.get(key.itemName) 
        price = Item.objects.all().filter(itemName=key.itemName)[0].price
        total+=int(itemCount[key.itemName])*price
        print(key.itemName, request.POST.get(key.itemName))

    customer  = Customer.objects.filter(name=user)
    # logic
    
    validShops =  Service.objects.filter(shopType = itemType).filter(numCust__lt=3).order_by('slotID')
    
    ##

    if customer[0].zone == 'Orange':
        validShops = Service.Objects.filter(shopType = itemType).filter(zone='Orange').filter(numCust__lt=3)
        validShops = validShops.append(Service.Objects.filter(shopType = itemType).filter(zone='Red').filter(numCust__lt=3))
    elif customer[0].zone == 'Red':
        validShops =  Service.objects.filter(shopType = itemType).filter(zone='Red').filter(zoneID=customer[0].zoneID).filter(numCust__lt=3).order_by('slotID')

    if request.session['site'] == 'Amazon' or request.session['site'] == 'Flipkart':
        validShops = Service.objects.filter(shopType = itemType)

    ##
    if(len(validShops) == 0):
        slot = "Try again later"
        shopName=""
        return render(request, 'output.html', {'name':user, 'shop_name':shopName, 'slot_time':slot, 'itemCount': itemCount, 'total':total, 'site':site})
    shopName = validShops[0].name
    _slot = validShops[0].slotID
    dist = math.sqrt((customer[0].lon - validShops[0].lon)**2 + (customer[0].lat - validShops[0].lat)**2)
    for shop in validShops:
        d = math.sqrt((customer[0].lon - shop.lon)**2 + (customer[0].lat - shop.lat)**2)
        if(dist < d):
            dist = d
            shopName = shop.name
            _slot = shop.slotID
    selectedshop = Service.objects.filter(name=shopName).filter(slotID=_slot)
    selectedshop[0].numCust = selectedshop[0].numCust + 1
    if _slot==1:
        _slot="10AM"
    elif _slot==2:
        _slot="11AM"
    else:
        slot="12AM"

    return render(request, 'output.html', {'name':user, 'shop_name':shopName, 'slot_time':_slot, 'itemCount': itemCount, 'total':total, 'site':site})

def delivery(request):
    if not request.user.is_authenticated:
        return redirect('/login')
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
    if not request.user.is_authenticated:
        return redirect('/login')
    item_list = Item.objects.all().filter(itemType='Fruits')
    return render(request, 'fruitsVeg.html',{'item_list':item_list})

def dairy(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    item_list = Item.objects.all().filter(itemType='Dairy')
    return render(request, 'dairy.html',{'item_list':item_list})

def medicine(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    item_list = Item.objects.all().filter(itemType='Medicine')
    return render(request, 'medicine.html',{'item_list':item_list})

def cereals_and_pulses(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    item_list = Item.objects.all().filter(itemType='Cereals')
    return render(request, 'cereals.html',{'item_list':item_list})

def amazon(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    request.session['site'] = 'Amazon'
    request.session['coun'] = 1
    return redirect('/pickup')

def flipkart(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    request.session['site'] = 'Flipkart'
    request.session['coun'] = 1
    return redirect('/pickup')
