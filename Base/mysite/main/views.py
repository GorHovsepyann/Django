from django.shortcuts import render
from .models import brend,car
# Create your views here.

def Home(request):
    brend_list = brend.objects.all()
    return render ( request,'home.html',context={
        'brend_list':brend_list
    })
    
def Car(request,id):
    car_filter = brend.objects.filter(pk=id)
    return render(request,'car.html',context={
        'car_filter':car_filter
    })
    
