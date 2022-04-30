# Generated by Django 4.0.4 on 2022-04-30 08:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commentaire_obs', models.CharField(max_length=255, unique=True)),
                ('observation', models.BooleanField()),
            ],
            options={
                'db_table': 'observation',
            },
        ),
    ]
