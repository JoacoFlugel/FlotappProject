# Generated by Django 3.2.9 on 2021-12-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('dominio', models.CharField(max_length=10)),
                ('conductores', models.IntegerField()),
            ],
        ),
    ]
