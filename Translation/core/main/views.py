from django.shortcuts import render
from .models  import product
# Create your views here.

def Home(request):
    product_list = product.objects.all()
    return render(request,'main/home.html',context={
        'product_list':product_list
    })