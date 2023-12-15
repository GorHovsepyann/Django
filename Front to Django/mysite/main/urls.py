from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('about/',views.About,name='about'),
    path('blog/',views.Blog,name='blog'),
    path('shop/',views.Shop,name='shop')
]