# Generated by Django 3.2.16 on 2022-10-27 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('carID', models.AutoField(primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('fuel_type', models.CharField(max_length=30)),
                ('colour', models.CharField(max_length=30)),
                ('license_plate', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('mileage', models.CharField(max_length=30)),
            ],
        ),
    ]