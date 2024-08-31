# Generated by Django 5.1 on 2024-08-25 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SanDiegoCurrentYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'san_diego_current_year',
            },
        ),
        migrations.CreateModel(
            name='SanDiegoNearbyAreaTrends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('median_rent', models.FloatField()),
                ('month', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='SanDiegoPrevYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'san_diego_prev_year',
            },
        ),
    ]
