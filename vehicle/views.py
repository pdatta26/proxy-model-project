from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializer import *


# Create your views here.


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class HondaViews(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = HondaSerializer

    def get_queryset(self):
        return Honda.objects.all()

# class HondaViewSet(ModelViewSet):
#     queryset = Honda.objects.all()
#     serializer_class = HondaSerializer
