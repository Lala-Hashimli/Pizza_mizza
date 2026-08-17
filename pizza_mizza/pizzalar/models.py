from django.db import models



class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2) 


    def __str__(self):
        return self.name