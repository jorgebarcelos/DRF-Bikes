# Generated by Django 3.2.15 on 2022-09-29 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bikes',
            options={'ordering': ['id'], 'verbose_name': 'Bike', 'verbose_name_plural': 'Bikes'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['id'], 'verbose_name': 'Score', 'verbose_name_plural': 'Scores'},
        ),
    ]
