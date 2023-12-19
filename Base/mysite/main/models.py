from django.db import models

# Create your models here.

class brend(models.Model):
    
    name = models.CharField('Brend Name',max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    
class car(models.Model):
    
    brend = models.ForeignKey(brend,on_delete=models.CASCADE,related_name='cat_prod')
    name = models.CharField('Car name',max_length=50)
    img = models.ImageField('Car image',upload_to='cars/')
    price = models.PositiveIntegerField('Car price')
    
    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'
