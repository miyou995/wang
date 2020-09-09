# Generated by Django 3.1 on 2020-08-24 17:32

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200813_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='fiche2',
            field=models.ImageField(blank=True, upload_to='product/fiche/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='fiche3',
            field=models.ImageField(blank=True, upload_to='product/fiche/'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='fiche',
            field=models.ImageField(blank=True, upload_to='product/fiche/'),
        ),
    ]