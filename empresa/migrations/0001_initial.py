# Generated by Django 2.0.7 on 2019-05-30 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminEmpresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='empresaDatos',
            fields=[
                ('nombreEmpresa', models.CharField(blank=True, max_length=70, null=True)),
                ('rutEmpresa', models.CharField(blank=True, max_length=12, primary_key=True, serialize=False)),
                ('rutAdmin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='adminEmpresa.adminDatos')),
            ],
        ),
    ]
