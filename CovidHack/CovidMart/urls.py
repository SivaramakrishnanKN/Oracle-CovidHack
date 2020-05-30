from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
        path('login/',views.login_request,name="login"),
    path('registration/', views.registerCustomer, name="registration"),
    path('map/', views.map, name="map"),
    path('Home/',views.Home, name="home")

]