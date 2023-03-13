# Generated by Django 4.0.6 on 2022-12-12 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_productmodel_is_fave'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0008_remove_cartitemmodel_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_Item_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_unit', models.PositiveIntegerField(blank=True, verbose_name='قیمت محصول')),
                ('quantity', models.IntegerField(default=1, verbose_name='تعداد محصول')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ایتم سبد',
                'verbose_name_plural': 'ایتم های سبد',
            },
        ),
        migrations.CreateModel(
            name='Cart_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveIntegerField(blank=True, verbose_name='قیمت کل محصولات این سبد خرید')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شد')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.RemoveField(
            model_name='cartmodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='CartItemModel',
        ),
        migrations.DeleteModel(
            name='CartModel',
        ),
        migrations.DeleteModel(
            name='DiscountModel',
        ),
        migrations.AddField(
            model_name='cart_item_model',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart_model', verbose_name='سبد خرید'),
        ),
        migrations.AddField(
            model_name='cart_item_model',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel', verbose_name='محصول'),
        ),
    ]