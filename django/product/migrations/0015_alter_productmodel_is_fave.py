# Generated by Django 4.0.6 on 2022-12-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_productmodel_is_fave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='is_fave',
            field=models.BooleanField(default=False, verbose_name='موردعلاقه'),
        ),
    ]