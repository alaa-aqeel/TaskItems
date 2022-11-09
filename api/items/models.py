from django.db import models

# Create your models here.

class Item(models.Model):
    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads")
    expired_at = models.DateTimeField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        
        return str(self.name)