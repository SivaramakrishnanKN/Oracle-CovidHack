from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
        path('login/',views.login_request,name="login"),
    path('registration/', views.registerCustomer, name="registration"),
    path('map/', views.map, name="map"),
    path('itemForm', views.itemForm, name="itemForm"),
    path('pickup/',views.pickup, name="pickup"),
    path('delivery/',views.delivery, name="delivery"),
    path('delivery/fruits_and_veg/',views.fruits_and_veg,name="fruits_and_veg"),
    path('delivery/dairy/',views.dairy,name="dairy"),
    path('delivery/medicine/',views.medicine,name="medicine"),
    path('delivery/cereals_and_pulses/',views.cereals_and_pulses,name="cereals_and_pulses"),
    path('pickup/fruits_and_veg/',views.fruits_and_veg,name="fruits_and_veg1"),
    path('pickup/dairy/',views.dairy,name="dairy1"),
    path('pickup/medicine/',views.medicine,name="medicine1"),
    path('pickup/cereals_and_pulses/',views.cereals_and_pulses,name="cereals_and_pulses1")

]