from django.shortcuts import render
from .models import Best_Jewellery,Latest_Products,About_Us
# Create your views here.


def Index(request):
    About = About_Us.objects.all().first()
    Product = Latest_Products.objects.all()
    Hndik = Best_Jewellery.objects.all().first()
    return render(request,'main/index.html',context={
        'Hndik':Hndik,
        'Product':Product,
        'About':About
    })
    
    
    
def About(request):
    About = About_Us.objects.all().first()
    return render(request,'main/about.html',context={
        'About':About
    })
def Blog(request):
    return render(request,'main/blog.html',context={
        
    })
def Shop(request):
    Product = Latest_Products.objects.all()
    return render(request,'main/shop.html',context={
        'Product':Product
    })