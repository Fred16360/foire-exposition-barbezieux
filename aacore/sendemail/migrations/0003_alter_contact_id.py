# Generated by Django 4.0 on 2022-08-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendemail', '0002_auto_20220820_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
