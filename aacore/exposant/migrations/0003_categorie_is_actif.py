# Generated by Django 4.0.1 on 2022-02-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exposant', '0002_alter_categorie_nom_categorie_alter_exposant_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='is_actif',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
