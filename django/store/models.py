from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import binascii
import os
from django.utils import timezone
from user.models import UserModel
from django.utils.html import mark_safe
from django.conf import settings
import base64
import io
from PIL import Image

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def Profile_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"logo_img/{final_name}"
    return x


# class StoreCategoryModel(models.Model):
#     title = models.CharField(max_length=50, verbose_name='دسته فروشگاهی')

#     created_at = models.DateTimeField(default=timezone.now, blank=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         verbose_name = ('دسته فروشگاهی')
#         verbose_name_plural = ('دسته فروشگاهی')

#     def __str__(self):
#         return self.title


class StoreModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    store_name = models.CharField(max_length=30, unique=True, verbose_name="نام فروشگاه")
    store_phone_number = models.CharField(max_length=8, verbose_name='تلفن فروشگاه', blank=True, null=True)
    address = models.TextField(verbose_name='آدرس')
    logo = models.ImageField(upload_to=Profile_image_path, null=True, blank=True, verbose_name="لوگو")

    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("فروشگاه ها ")
        verbose_name_plural = ("فروشگاه")

    def __str__(self):
        return self.store_name


    def image_tag(self):
        if self.logo != '':
            return mark_safe('<img src="%s%s" width="45" height="45" />' % (f'{settings.MEDIA_URL}', self.logo))


class SmsModel(models.Model):
    phone = models.CharField(max_length=11, verbose_name='شماره موبایل')
    sms = models.CharField(max_length=6, verbose_name='SMS')

    class Meta:
        verbose_name = ("اس ام اس")
        verbose_name_plural = ("اس ام اس")

    def __str__(self):
        return f'{self.phone} ---- {self.sms}'

