from rest_framework import serializers
from .models import *

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        # fields = "__all__"
        exclude = ['created_at', 'updated_at']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateModel
        # fields = "__all__"
        exclude = ['created_at', 'updated_at']

class CommentsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = "__all__"
        depth = 2
        
                
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteModel
        # fields = "__all__"
        exclude = ['created_at', 'updated_at']
        