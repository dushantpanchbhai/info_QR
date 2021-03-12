from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=None)

    def __str__(self):
        return self.name

class Qr(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='QR_images/')

    def __str__(self):
        return self.name
    
# Create your models here.
