from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import *


class StoreSerializer(serializers.ModelSerializer):
    logo = Base64ImageField()

    class Meta:
        model = StoreModel
        fields = "__all__"

    def create(self, validated_data):
        return StoreModel.objects.create(**validated_data)



class StoreSerializer2(serializers.ModelSerializer):
    logo = Base64ImageField()

    class Meta:
        model = StoreModel
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        return StoreModel.objects.create(**validated_data)

# class StoreCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StoreCategoryModel
#         fields = "__all__"

class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsModel
        fields = "__all__"
