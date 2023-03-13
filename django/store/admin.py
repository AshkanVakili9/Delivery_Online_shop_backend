from django.contrib import admin
from .models import *

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    fields = ['user','store_name','store_phone_number', 'address', 'logo']
    list_display = ['user', 'store_name','store_phone_number', 'image_tag']
    search_fields = ['user', 'store_name', 'store_phone_number']
    list_filter = ['user', 'store_phone_number', 'created_at']




admin.site.register(StoreModel, StoreAdmin)
# admin.site.register(StoreCategoryModel)
admin.site.register (SmsModel)