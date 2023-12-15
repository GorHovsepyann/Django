from django.db import models

# Create your models here.

class Support(models.Model):
    
    name = models.CharField('Support name',max_length=50)
    email = models.EmailField('Support email')
    text = models.TextField('Support text')
    
    def __str__(self) -> str:
        return self.name
    
