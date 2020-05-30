from django import forms 

from .models import Customer
  
# create a ModelForm 
class CustomerForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Customer 
        fields = "__all__"