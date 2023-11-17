from .models import *
from rest_framework import serializers
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = "__all__"