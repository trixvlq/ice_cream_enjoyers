from rest_framework import serializers

from icecream.models import IceCream


class IceCreamSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = IceCream
        fields = '__all__'