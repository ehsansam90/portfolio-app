# Generated by Django 5.1 on 2024-09-10 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_surveyquestion_surveyresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='question_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('rating', 'Rating'), ('multiple_choice', 'Multiple Choice')], max_length=20),
        ),
        migrations.CreateModel(
            name='SurveyOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='main.surveyquestion')),
            ],
        ),
        migrations.DeleteModel(
            name='SurveyResponse',
        ),
    ]
