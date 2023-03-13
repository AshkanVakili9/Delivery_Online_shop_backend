from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
import os
from django.conf import settings
from django.utils.html import mark_safe

from .managers import CustomUserManager


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def Profile_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"profile-img/{final_name}"
    return x


class SmsModel(models.Model):
    phone = models.CharField(max_length=11, verbose_name='شماره موبایل')
    sms = models.CharField(max_length=6, verbose_name='SMS')

    class Meta:
        verbose_name = ("اس ام اس")
        verbose_name_plural = ("اس ام اس")

    def __str__(self):
        return f'{self.phone} ---- {self.sms}'


class UserModel(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='نام')
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=' نام خانوادگی')
    phone = models.CharField(
        max_length=11, verbose_name='شماره موبایل', unique=True, blank=False, null=False)
    password = models.CharField(
        max_length=100, verbose_name='رمز', blank=False, null=False)
    address = models.TextField(verbose_name='آدرس')
    image = models.ImageField(upload_to=Profile_image_path,
                              blank=True, null=True, verbose_name=' عکس ‍‍‍‍‍‍‍‍پروفایل')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_store = models.BooleanField(default=False)
    is_verifed = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = ("کاربر")
        verbose_name_plural = ("کاربران")

    def __str__(self):
        return f"{self.first_name}  ---  {self.phone}"

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="45" height="45" />' % (f'{settings.MEDIA_URL}', self.image))
