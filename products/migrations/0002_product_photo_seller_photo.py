# Generated by Django 4.2.4 on 2023-08-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='product/photos/'),
        ),
        migrations.AddField(
            model_name='seller',
            name='photo',
            field=models.ImageField(null=True, upload_to='seller/photos/'),
        ),
    ]
