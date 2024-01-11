from django.db import models
from django.db import models
# Create your models here.
#item, car_make, model_number, Price

class CarDetails(models.Model):
    item_name = models.CharField(max_length = 30, verbose_name='Item Name')
    car_make = models.CharField(max_length = 30, verbose_name='Car Make')
    model_number = models.CharField(max_length = 30, verbose_name='Model Number')
    price = models.FloatField(max_length = 30, verbose_name='Price')
    created = models.DateTimeField(verbose_name='created', auto_now_add=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = "Car Details"
