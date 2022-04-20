# Generated by Django 4.0.4 on 2022-04-20 15:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entreprise', '0001_initial'),
        ('observation', '0001_initial'),
        ('motifs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ref', models.CharField(max_length=255, unique=True)),
                ('projet', models.CharField(max_length=255, unique=True)),
                ('etat_projet', models.BooleanField()),
                ('entree', models.DateTimeField(null=True)),
                ('livree', models.DateTimeField(null=True)),
                ('code_fichier', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=100)),
                ('entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entreprise.entreprise')),
                ('motifs', models.ManyToManyField(blank=True, to='motifs.motifs')),
                ('observation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='observation.observation')),
            ],
            options={
                'db_table': 'projects',
            },
        ),
    ]
