# Generated by Django 2.0.7 on 2019-06-03 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresadatos',
            name='rutAdmin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminEmpresa.adminDatos'),
        ),
    ]
