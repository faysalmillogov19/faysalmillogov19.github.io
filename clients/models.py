from django.db import models

# Create your models here.
class Client(models.Model):
    nom= models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    date_naiss = models.DateField()
    sexe = models.CharField(max_length=2)
    telephone = models.CharField(max_length=20)
    date_sous = models.DateField()
    created= models.TimeField(auto_now=False, auto_now_add=True)
    updated= models.TimeField(auto_now=True, auto_now_add=False)



