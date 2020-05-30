from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Item 


def index(request):
    return render(request, "index.html")


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

     
def Home(request):
    item_list = Item.objects.all()
    items = {}
    count = 0
    return render(request,'Home.html',{'item_list':item_list})


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