# Generated by Django 3.2.15 on 2022-09-27 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('model_name', models.CharField(max_length=100, unique=True)),
                ('engine_power', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Bike',
                'verbose_name_plural': 'Bikes',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('person_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(blank=True, default='')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='motorcycles.bikes')),
            ],
            options={
                'verbose_name': 'Score',
                'verbose_name_plural': 'Scores',
                'unique_together': {('email', 'bike')},
            },
        ),
    ]
