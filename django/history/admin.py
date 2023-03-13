from django.contrib import admin
from .models import *
# Register your models here.


# class LikeAdmin(admin.ModelAdmin):
#     exclude=("likes_number ",)
#     readonly_fields=('likes_number', )




admin.site.register(CommentsModel)
admin.site.register(FavoriteModel)
admin.site.register(RateModel)
# admin.site.register(LikeModel)