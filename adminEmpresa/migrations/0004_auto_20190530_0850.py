# Generated by Django 2.0.7 on 2019-05-30 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminEmpresa', '0003_auto_20190530_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindatos',
            name='id_tipoUsuario',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminEmpresa.tipoUsuario'),
        ),
    ]
