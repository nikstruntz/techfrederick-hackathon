# Generated by Django 3.0.7 on 2020-06-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='bls_bag',
            field=models.BooleanField(verbose_name='BLS Bag'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='date',
            field=models.DateField(help_text='Please display in the form yyyy-mm-dd!'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='driving_lights',
            field=models.BooleanField(verbose_name='Driving Lights'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='emergency_lights',
            field=models.BooleanField(verbose_name='Emergency Lights'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='fuel',
            field=models.CharField(help_text='Please enter E for empty or F for full.', max_length=1),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='lp_fifteen',
            field=models.BooleanField(verbose_name='LP 15'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='oxygen_bag',
            field=models.BooleanField(verbose_name='Oxygen Bag'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='red_bag',
            field=models.BooleanField(verbose_name='Red Bag'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='rtf_bags',
            field=models.BooleanField(verbose_name='RTF Bags'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='signature',
            field=models.CharField(max_length=50, verbose_name='Provider Signature'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='trans_box',
            field=models.BooleanField(verbose_name='Trans Box'),
        ),
    ]
