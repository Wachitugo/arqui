# Generated by Django 4.2.1 on 2023-07-07 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CIUDAD',
            fields=[
                ('id_ciudad', models.AutoField(db_column='idciudad', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='USUARIO',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('contra', models.CharField(max_length=30)),
                ('saldo', models.CharField(max_length=6)),
                ('correo', models.CharField(max_length=50)),
                ('id_ciudad', models.ForeignKey(db_column='idciudad', on_delete=django.db.models.deletion.CASCADE, to='usuarios.ciudad')),
            ],
        ),
    ]