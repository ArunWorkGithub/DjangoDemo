from rest_framework import serializers
from django_demo_app.models import Drinks

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields =  ['id', 'name', 'description']