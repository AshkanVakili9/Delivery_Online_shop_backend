# Generated by Django 4.0.6 on 2022-12-10 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_discountmodel_alter_cartmodel_is_paid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitemmodel',
            name='quantity',
        ),
    ]
