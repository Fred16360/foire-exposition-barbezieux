# Generated by Django 4.0.1 on 2022-02-21 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField()),
                ('nom_categorie', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('numero',),
            },
        ),
        migrations.CreateModel(
            name='Exposant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_exposant', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('code_postal', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=30)),
                ('num_tel', models.CharField(max_length=20)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exposant.categorie')),
            ],
            options={
                'ordering': ('nom_exposant',),
            },
        ),
    ]
