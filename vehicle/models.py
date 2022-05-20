from django.db import models


# Create your models here.
class CarManager(models.Manager):
    def get_queryset(self):
        return


class Car(models.Model):
    model = models.CharField(max_length=100, blank=False, null=False)
    brand = models.CharField(max_length=100, blank=False, null=False)
    wheel = models.CharField(max_length=100, blank=False, null=False)


class HondaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(model="Honda")


class PrivetCarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(model="PrivetCar")


class Honda(Car):
    objects = HondaManager()

    class Meta:
        proxy = True


class PrivetCar(Car):
    objects = PrivetCarManager()

    class Meta:
        proxy = True
