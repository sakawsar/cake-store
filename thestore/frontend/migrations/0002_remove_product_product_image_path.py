# Generated by Django 5.0.4 on 2024-10-18 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image_path',
        ),
    ]
