# Generated by Django 4.0.4 on 2022-04-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debloqueur', '0009_alter_debloqueur_date_deblocage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debloqueur',
            name='date_deblocage',
            field=models.DateTimeField(),
        ),
    ]
