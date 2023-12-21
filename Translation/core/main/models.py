from django.db import models

# Create your models here.

class product(models.Model):
    
    name = models.CharField('Product name',max_length=50)
    about = models.TextField('Product text')
    img = models.ImageField('Product images',upload_to='')
    
    def __str__(self) -> str:
        return self.name