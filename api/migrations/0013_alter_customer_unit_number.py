# Generated by Django 3.2.16 on 2022-10-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_rental_gold_member_rental_cid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='unit_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
