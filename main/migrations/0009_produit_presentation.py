# Generated by Django 3.1 on 2020-08-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_produit_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='presentation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
