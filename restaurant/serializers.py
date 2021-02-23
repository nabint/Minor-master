from rest_framework import serializers
from restaurant import models

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Table
        fields = '__all__'