# Generated by Django 5.1 on 2024-09-11 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_surveyquestion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
