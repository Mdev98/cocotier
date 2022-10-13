# Generated by Django 4.1.1 on 2022-09-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fraud',
            name='type_fraud',
            field=models.CharField(choices=[('VOL', 'Vol'), ('PERTE', 'Perte'), ('ARNAQUE', 'Arnaque')], max_length=7, verbose_name='type de fraude'),
        ),
    ]
