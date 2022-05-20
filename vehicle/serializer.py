from rest_framework.serializers import ModelSerializer
from .models import *


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class HondaSerializer(ModelSerializer):
    class Meta:
        model = Honda
        fields = ['model', 'brand', 'wheel']
