# Generated by Django 4.0.6 on 2022-07-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='main.menu'),
        ),
    ]
