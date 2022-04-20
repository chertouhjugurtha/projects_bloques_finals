# Generated by Django 4.0.4 on 2022-04-20 15:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ministere', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debloqueur',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255, unique=True)),
                ('prenom', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=255, unique=True)),
                ('qualite', models.CharField(max_length=255, unique=True)),
                ('bureau', models.CharField(max_length=255, unique=True)),
                ('dtdebloqueur',  models.CharField(max_length=255, unique=True)),
                ('ministere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ministere.ministere')),
            ],
            options={
                'db_table': 'debloqueur',
            },
        ),
    ]
