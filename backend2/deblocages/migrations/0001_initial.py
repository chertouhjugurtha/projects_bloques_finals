# Generated by Django 4.0.4 on 2022-04-21 07:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('debloqueur', '0002_remove_debloqueur_dtdebloqueur'),
        ('motifs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deblocages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dt_dablocage', models.DateField()),
                ('deblocage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debloqueur.debloqueur')),
                ('motif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motifs.motifs')),
            ],
            options={
                'db_table': 'deblocages',
            },
        ),
    ]
