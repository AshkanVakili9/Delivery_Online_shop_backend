from django.contrib import admin
from .models import *
# Register your models here.

class Cart_Admin(admin.ModelAdmin):

    list_display = ['pk','user', 'total_price', 'is_paid']
    readonly_fields= ['is_paid', 'total_price']


class Cart_Item_Admin(admin.ModelAdmin):

    list_display = ['pk','product', 'quantity','cart']


admin.site.register(Cart_Model, Cart_Admin)
admin.site.register(Cart_Item_Model, Cart_Item_Admin)
# admin.site.register(Discount_Model)
# admin.site.register(Payment_Details)
# admin.site.register(Order_Datails)
# admin.site.register(Order_Items)
# admin.site.register(Order_Items)
# admin.site.register(Discount)
