from rest_framework import serializers
from .models import Modelo_1, Modelo_2

class Modelo_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo_1
        fields = '__all__'

class Modelo_2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo_2
        fields = '__all__'