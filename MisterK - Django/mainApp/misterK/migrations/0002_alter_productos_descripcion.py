# Generated by Django 5.1 on 2024-11-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misterK', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]