import django_filters
from .models import *
from django_filters import *
# from django_filters.rest_framework import DjangoFilterBackend, RangeFilter, FilterSet, filters


# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = ProductModel
#         fields = ['price',]



""" /api/?price_min=13&price_max=31&brand=asus&ram_min=2&ram_max=8 """



class PriceFilter(django_filters.FilterSet):
    price = filters.RangeFilter()
    ram = filters.RangeFilter()

    class Meta:
        model = ProductModel
        fields = ['price', 'brand', 'ram', 'cpu_creator', 'condition']