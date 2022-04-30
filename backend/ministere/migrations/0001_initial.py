# Generated by Django 4.0.4 on 2022-04-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministere',
            fields=[
                ('ministere', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ministere',
            },
        ),
    ]
