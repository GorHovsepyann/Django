from django.db import models

# Create your models here.

class Best_Jewellery(models.Model):
    
    name = models.CharField('Hndik name',max_length=60)
    button_name = models.CharField('Hndik button name',max_length=50)
    about = models.TextField('About hndik')
    img = models.ImageField('Hndik image' , upload_to='images')
    
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Latest_Products(models.Model):
    
    img = models.ImageField('Product image',upload_to='images')
    name = models.CharField('Product name',max_length=50)
    price = models.PositiveIntegerField('Product price')
    active = models.BooleanField('Product active')
    
    def __str__(self) -> str:
        return self.name
    
class About_Us(models.Model):
    
    name = models.CharField('About name',max_length=50)
    button_name = models.CharField('Button name',max_length=50)
    img = models.ImageField('About img',upload_to='images')
    about = models.TextField('About text')
    
    def __str__(self) -> str:
        return self.name