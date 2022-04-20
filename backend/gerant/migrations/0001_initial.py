# Generated by Django 4.0.4 on 2022-04-20 11:49

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gerant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255, unique=True)),
                ('prenom', models.CharField(max_length=255, unique=True)),
                ('age', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('date_naissance', models.DateField(null=True)),
                ('phone', models.CharField(max_length=100)),
                ('nationalite', models.CharField(max_length=100)),
                ('gerant', models.BooleanField()),
            ],
            options={
                'db_table': 'grant',
            },
        ),
    ]