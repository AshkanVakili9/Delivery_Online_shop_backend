from django.db import models
from user.models import *
from product.models import ProductModel
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# from cart.models import CartModel
# Create your models here.


"""Add a new rating  for our products"""
class RateModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} --- {self.product.name} --- {self.rate}"

    class Meta:
        verbose_name = ("امتیاز")
        verbose_name_plural = ("امتیاز ها")


"""Add a new Comment  for our products"""
class CommentsModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول', related_name='comments')
    coments = models.TextField(verbose_name='نظرات')

    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} --- {self.product.name}"

    class Meta:
        verbose_name = (" نظر")
        verbose_name_plural = (" نظرات")


"""Add a new product to user favorite tabel."""
class FavoriteModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} ---- {self.product.name}"

    class Meta:
        verbose_name = ('مورد علاقه')
        verbose_name_plural = ('مورد علاقه ها')


# class LikeModel(models.Model):
#     likes = models.BooleanField(default=False)
#     product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.user.first_name} --- {self.favorite_product}"

#     class Meta:
#         verbose_name = ('لایک')
#         verbose_name_plural = ('لایک')


# class PurchaseItems(models.Model):
#     items = models.ForeignKey(CartModel, on_delete=models.CASCADE)
