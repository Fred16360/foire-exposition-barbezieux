# Generated by Django 4.0 on 2022-08-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exposant', '0005_auto_20220820_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='exposant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]