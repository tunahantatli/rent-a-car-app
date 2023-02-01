from django.db import models
from django.core.validators import MinValueValidator
from users.serializers import User

# Create your models here.
class Car(models.Model):
    Gear = (
        ('a', 'automatic'),
        ('m', 'manual'),
    )
    plate_number = models.CharField(max_length=15, unique=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=1, choices=Gear)
    rent_per_day = models.DecimalField(
        max_digits=6, # for price 
        decimal_places=2,
        validators = [MinValueValidator(1)]
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.plate_number}-{self.brand}-{self.model}-{self.gear}-{self.rent_per_day}'

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'customers')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name= 'cars')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'Customer:{self.customer}-Reserved: {self.car}- Start Date: {self.start_date}- End Date: {self.end_date}'