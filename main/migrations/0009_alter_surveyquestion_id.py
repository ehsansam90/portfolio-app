# Generated by Django 5.1 on 2024-09-11 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_option_surveysubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
