# Generated by Django 4.0.6 on 2022-12-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_cart_item_model_cart_model_remove_cartmodel_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart_model',
            options={'verbose_name': ' سبد', 'verbose_name_plural': ' سبد'},
        ),
        migrations.AlterField(
            model_name='cart_model',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت کل محصولات این سبد خرید'),
        ),
    ]
