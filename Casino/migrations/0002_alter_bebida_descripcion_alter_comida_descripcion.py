# Generated by Django 4.2.1 on 2023-06-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Casino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comida',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
