from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import *




class UserSerializer(serializers.ModelSerializer):
    image = Base64ImageField()


    class Meta:
        model = UserModel
        fields = '__all__'
        
    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class SmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SmsModel
        fields = '__all__'
