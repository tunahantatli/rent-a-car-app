from django.db import models

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
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.plate_number}-{self.brand}-{self.model}-{self.gear}-{self.rent_per_day}'
