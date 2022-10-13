# Generated by Django 4.1.1 on 2022-09-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monetique', '0004_controlemonetique_ecart_comptabilite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlemonetique',
            name='ecart_comptabilite',
            field=models.IntegerField(default=0, verbose_name='ecart comptabilite'),
        ),
        migrations.AlterField(
            model_name='controlemonetique',
            name='ecart_comptabilite_compte_cantonnement',
            field=models.IntegerField(default=0, verbose_name='ecart comptabilite comptabilite'),
        ),
        migrations.AlterField(
            model_name='controlemonetique',
            name='ecart_compte_cantonnement',
            field=models.IntegerField(default=0, verbose_name='ecart compte de cantonnement'),
        ),
    ]
