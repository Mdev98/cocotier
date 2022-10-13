# Generated by Django 4.0.6 on 2022-07-19 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeclarationReclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('nbr_global_reclamation_enregistre', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='nombre global de reclamations enregistrées')),
                ('nbr_global_reclamation_traite', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='nombre global de reclamations traitées')),
                ('nbr_reclamation_enregistre', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='nombre de reclamations enregistrées')),
                ('motif_reclamation', models.TextField(verbose_name='motif de la reclamation')),
                ('nbr_reclamation_traite', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='nombre de reclamations traitées')),
            ],
        ),
    ]
