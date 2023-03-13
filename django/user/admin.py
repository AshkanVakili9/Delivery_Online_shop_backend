from django.contrib import admin

from .models import *
# from django.utils.html import format_html

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'phone', 'image', 'password', 'address',
              'is_staff', 'is_superuser', 'is_active', 'is_store', 'is_verifed', 'date_joined']

    list_display = ['first_name', 'last_name','phone', 'image_tag']

    search_fields = ['first_name', 'last_name', 'phone']
    
    list_filter = ['is_staff', 'is_active','is_store', 'is_verifed', 'date_joined']


admin.site.register(UserModel, UserAdmin)
admin.site.register(SmsModel)
