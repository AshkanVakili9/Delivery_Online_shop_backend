from django.db import models
from store.models import StoreModel
from django.utils import timezone
import os
from django.utils.html import mark_safe
from django.conf import settings
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def Profile_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"product_image/{final_name}"
    return x


class TagModel(models.Model):
    tag = models.CharField(max_length=40)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = (" تگ")
        verbose_name_plural = (" تگ ها")


class CategoryModel(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = (" دسته محصول")
        verbose_name_plural = ("دسته محصولات")


class SubCategoryModel(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = (" زیر دسته محصول")
        verbose_name_plural = ("زیر دسته محصولات")


class SubSubCategoryModel(models.Model):
    title = models.CharField(max_length=30)
    SubCategoryModel = models.ForeignKey(
        SubCategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("زیر زیر دسته محصول")
        verbose_name_plural = ("زیر زیر دسته محصول")


class BrandModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("برند محصول")
        verbose_name_plural = ("برند محصول")
 
 
        
class CPU_CHOICES_MODEL(models.Model):
    cpu_creator = models.CharField(max_length=50, verbose_name='سازنده پردازنده')
    
    def __str__(self):
        return self.cpu_creator

    class Meta:
        verbose_name = ('مدل پردازنده')
        verbose_name_plural = ('مدل پردازنده')




class ProductModel(models.Model):
    name = models.CharField(max_length=40, verbose_name='اسم محصول')
    weight = models.CharField(
        max_length=40, verbose_name='وزن', blank=True, null=True)
    size = models.CharField(
        max_length=40, verbose_name='ابعاد', blank=True, null=True)
    cpu_creator = models.CharField(
        max_length=40, verbose_name='سازنده پردازنده')
    cpu_series = models.CharField(max_length=40, verbose_name='سری پردازنده')
    cpu_model = models.CharField(max_length=40, verbose_name='مدل پردازنده', blank=True, null=True)
    cpu_speed_range = models.CharField(
        max_length=40, verbose_name='محدوده سرعت پردازنده', blank=True, null=True)
    processor_frequency = models.CharField(
        max_length=40, verbose_name='فرکانس پردازنده', blank=True, null=True)
    cache_memory = models.CharField(
        max_length=40, verbose_name='حافظه Cache', blank=True, null=True)
    extra_cpu_des = models.CharField(
        max_length=40, verbose_name='سایر توضیحات پردازنده مرکزی (CPU)', blank=True, null=True)
    ram = models.CharField(max_length=40, verbose_name='ظرفیت حافظه RAM')
    ram_type = models.CharField(
        max_length=6, verbose_name='نوع حافظه RAM')
    extra_ram_des = models.CharField(
        max_length=40, verbose_name='سایر توضیحات حافظه RAM', blank=True, null=True)
    internal_memory_capacity = models.CharField(
        max_length=40, verbose_name='ظرفیت حافظه داخلی')
    internal_memory_type = models.CharField(
        max_length=40, verbose_name='نوع حافظه داخلی')
    extra_internal_memory_des = models.CharField(
        max_length=40, verbose_name='سایر توضیحات حافظه داخلی', blank=True, null=True)
    gpu_manufacturer = models.CharField(
        max_length=40, verbose_name='سازنده پردازنده گرافیکی')
    gpu_model = models.CharField(
        max_length=40, verbose_name='مدل پردازنده گرافیکی')
    gpu_memory = models.CharField(
        max_length=40, verbose_name='حافظه اختصاصی پردازنده گرافیکی')
    screen_size = models.CharField(
        max_length=40, verbose_name='اندازه صفحه نمایش')
    screen_resolution = models.CharField(
        max_length=40, verbose_name='دقت صفحه نمایش')
    screen_resolution_des = models.CharField(
        max_length=40, verbose_name='توضیحات صفحه نمایش', blank=True, null=True)
    device_capabilities = models.CharField(
        max_length=40, verbose_name='قابلیت‌های دستگاه', blank=True, null=True)
    optical_drive = models.CharField(
        max_length=40, verbose_name='درایو نوری')
    speaker_description = models.CharField(
        max_length=40, verbose_name='مشخصات اسپیکر', blank=True, null=True)
    ports = models.CharField(
        max_length=2, verbose_name='درگاه‌های ارتباطی', blank=True, null=True)
    usb_2_ports = models.CharField(
        max_length=2, verbose_name='تعداد پورت USB 2.0', blank=True, null=True)
    usb_3_ports = models.CharField(
        max_length=10, verbose_name='تعداد پورت USB 3.2', blank=True, null=True)
    classification = models.CharField(
        max_length=40, verbose_name='طبقه‌بندی')
    battery_type = models.CharField(max_length=40, verbose_name='نوع باتری')
    battery_description = models.CharField(
        max_length=40, verbose_name='توضیحات باتری', blank=True, null=True)
    operating_system = models.CharField(
        max_length=40, verbose_name='سیستم عامل')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت محصول')
    description = models.TextField(
        verbose_name='توضیحات', blank=True, null=True)
    quantity = models.PositiveIntegerField(
        default=0, verbose_name='تعداد محصول', blank=True, null=True)
    condition = models.CharField(
        max_length=20, verbose_name='وضعیت لب تاب')
    subcategory = models.ForeignKey(
        SubCategoryModel, on_delete=models.CASCADE, verbose_name=" زیر دسته محصول")
    brand = models.ForeignKey(
        BrandModel, on_delete=models.CASCADE, verbose_name="برند محصول")
    store = models.ForeignKey(StoreModel, on_delete=models.CASCADE)
    tags = models.ForeignKey(
        TagModel, on_delete=models.CASCADE, verbose_name="تگ محصول")
    show_image = models.ImageField(upload_to = Profile_image_path, null=True, verbose_name=' اولیه عکس')
    offer = models.IntegerField(
        default=0, null=True, verbose_name="تخفیف محصول ")
    rate = models.IntegerField(default=0, blank=True, verbose_name="امتیاز")
    is_fave = models.BooleanField(default=False, verbose_name="موردعلاقه")
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = (" محصول")
        verbose_name_plural = (" محصولات")

    def image(self):
        if self.show_image != '':
            return mark_safe('<img src="%s%s" width="45" height="45" />' % (f'{settings.MEDIA_URL}', self.show_image))






class ProductImage(models.Model):
    name = models.CharField(max_length=30, verbose_name='نام')
    image = models.ImageField(upload_to = Profile_image_path, null=True, verbose_name='عکس های اضافی')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name= 'محصول', related_name='extra_image')

    def __str__(self):
        return self.name

    # def image(self):
    #     if self.image != '':
    #         return mark_safe('<img src="%s%s" width="45" height="45" />' % (f'{settings.MEDIA_URL}', self.image))

    class Meta:
        verbose_name = ("عکس محصول")
        verbose_name_plural = ("عکس محصول")