# Generated by Django 3.1.6 on 2021-02-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210213_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='qr',
            name='image',
            field=models.ImageField(upload_to='QR_images/'),
        ),
    ]
