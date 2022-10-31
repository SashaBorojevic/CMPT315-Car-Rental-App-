# Generated by Django 3.2.16 on 2022-10-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('drivers_license', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=200)),
                ('customer_phone', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('goldMember', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('province', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=30)),
                ('street_number', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('unit_number', models.CharField(max_length=30)),
            ],
        ),
    ]
