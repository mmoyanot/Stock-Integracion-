# Generated by Django 2.0.7 on 2019-05-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminDatos',
            fields=[
                ('nomAdmin', models.CharField(blank=True, max_length=70, null=True)),
                ('rutAdmin', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('emailAdmin', models.CharField(blank=True, max_length=70, null=True)),
                ('passAdmin', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]
