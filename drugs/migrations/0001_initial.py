# Generated by Django 3.0.7 on 2020-06-22 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shift_hours', models.DurationField()),
                ('rsi_kit_seal_number', models.CharField(max_length=5)),
                ('expiration_date', models.DateField()),
                ('incident_number', models.CharField(max_length=9)),
                ('hospital_number', models.CharField(max_length=5)),
                ('provider_name', models.CharField(max_length=30)),
                ('contact_bc_cole', models.DateTimeField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle')),
            ],
        ),
    ]