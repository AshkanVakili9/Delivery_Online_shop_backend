# Generated by Django 4.0.6 on 2022-11-26 09:07

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productimage_image_productimage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product_image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.productmodel', verbose_name='محصول'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='show_image',
            field=models.ImageField(null=True, upload_to=product.models.Profile_image_path, verbose_name=' اولیه عکس'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to=product.models.Profile_image_path, verbose_name='عکس های اضاقی'),
        ),
    ]