# Generated by Django 4.0.6 on 2023-01-02 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_cart_item_model_increment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item_model',
            name='increment_count',
        ),
    ]
