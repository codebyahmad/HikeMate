# Generated by Django 5.0 on 2023-12-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='avg_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='popularity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True),
        ),
    ]