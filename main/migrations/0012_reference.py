# Generated by Django 3.1 on 2020-08-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200809_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='ref/')),
                ('logo_noir', models.ImageField(upload_to='ref/')),
            ],
        ),
    ]
