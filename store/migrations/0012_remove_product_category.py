# Generated by Django 3.0.2 on 2020-11-26 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
