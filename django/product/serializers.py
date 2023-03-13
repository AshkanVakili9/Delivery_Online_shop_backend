from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import *
# from history.serializers import CommentsSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = "__all__"
        depth = 2


class SubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSubCategoryModel
        fields = "__all__"
        depth = 1


class ProductImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(represent_in_base64=True)
    class Meta:
        model = ProductImage
        fields = "__all__"

    def create(self, validated_data):
        return ProductImage.objects.create(**validated_data)


"""this one only works for get_all_products"""
class ProductSerializer(serializers.ModelSerializer):
    # show_image = Base64ImageField(represent_in_base64=True)
    show_image = Base64ImageField()
    class Meta:
        model = ProductModel
        fields = ["id", "name", "show_image", "price", "condition", 'is_fave','rate']
        

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)


""" get all detailes """
class ProductSerializer1(serializers.ModelSerializer):
    extra_image = ProductImageSerializer(many=True, read_only=True)

    """because of the too many comments cant use this mehtod but for use it need a related_name """ 
    # comments = CommentsSerializer(many=True, read_only=True)
    
    show_image = Base64ImageField()
    class Meta:
        model = ProductModel
        fields = "__all__"
        # depth =1

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)



