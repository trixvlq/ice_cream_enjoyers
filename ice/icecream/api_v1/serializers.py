from rest_framework import serializers

from icecream.models import IceCream, slugification, Category


class IceCreamSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = IceCream
        fields = '__all__'
        read_only_fields = ['saves','slug']
    def create(self, validated_data):
        title = validated_data['title']
        slug = slugification(title)
        validated_data['slug'] = slug
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'