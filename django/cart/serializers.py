from rest_framework import serializers
from .models import *


class Cart_Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Item_Model
        fields = "__all__"


class Cart_Serializers(serializers.ModelSerializer):
    cart_items = Cart_Item_Serializer(many=True, read_only=True)
    class Meta:
        model = Cart_Model
        fields = '__all__'



