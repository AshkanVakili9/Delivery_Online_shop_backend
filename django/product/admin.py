from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):


    readonly_fields=('rate', )
    list_display = ['pk','name', 'cpu_series', 'ram', 'image']
    search_fields = ['subcategory', 'store', 'tags']
    list_filter = ['cpu_creator','cpu_model', 'cache_memory',
                   'ram', 'ram_type','internal_memory_capacity', 'internal_memory_type',
                   'gpu_manufacturer', 'gpu_model', 'gpu_memory', 'screen_size',
                   'screen_resolution', 'device_capabilities', 'optical_drive',
                   'classification', 'battery_type', 'operating_system',
                   'price', 'description', 'quantity', 'condition',
                   'subcategory', 'brand', 'store', 'tags', 'offer']


admin.site.register(CategoryModel)
admin.site.register(SubCategoryModel)
admin.site.register(SubSubCategoryModel)
admin.site.register(BrandModel)
admin.site.register(ProductImage)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(TagModel)
