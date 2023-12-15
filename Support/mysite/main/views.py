from django.shortcuts import render,redirect
from .models import Support
# Create your views here.

def Index(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_text = request.POST.get('text')
        Support.objects.create(name = user_name,email = user_email,text = user_text)
        return redirect('index')
    return render(request,'index.html',context={
        
    })