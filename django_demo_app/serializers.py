from rest_framework import serializers
from django_demo_app.models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields =  ['id', 'name', 'description']