# Generated by Django 3.1 on 2020-08-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200824_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image_test',
            field=models.ImageField(blank=True, upload_to='product/'),
        ),
    ]
