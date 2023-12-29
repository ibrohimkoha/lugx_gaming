from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name ='registration/signup.html'

   
  
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request,'shop.html')

def product_details(request):
    return render(request,'product-details.html')
