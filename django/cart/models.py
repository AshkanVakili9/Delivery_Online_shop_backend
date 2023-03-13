from django.db import models
from user.models import UserModel
from product.models import ProductModel
from store.models import StoreModel
from django.utils import timezone

# Create your models here.

class Cart_Model(models.Model):
   user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
   total_price = models.PositiveIntegerField(blank=True, null=True ,verbose_name='قیمت کل محصولات این سبد خرید') 
   is_paid = models.BooleanField(default=False, verbose_name='پرداخت شد')

   created_at = models.DateTimeField(default=timezone.now, blank=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
        verbose_name = (' سبد')
        verbose_name_plural = (' سبد')
   
   def __str__(self):
      return f"{self.user.first_name} --- {self.user.last_name} --- {self.user.phone}"



class Cart_Item_Model(models.Model):
   product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
   cart = models.ForeignKey(Cart_Model, on_delete=models.CASCADE, verbose_name='سبد خرید', related_name='cart_items')
   quantity = models.IntegerField(default=1, verbose_name='تعداد محصول')


   created_at = models.DateTimeField(default=timezone.now, blank=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
      return f"{self.product.name} --- {self.product.quantity}"
   
   class Meta:
        verbose_name = ('ایتم سبد')
        verbose_name_plural = ('ایتم های سبد')



