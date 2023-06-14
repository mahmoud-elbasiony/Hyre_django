# Generated by Django 4.2.2 on 2023-06-13 21:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tenant', '0004_alter_applicant_status_alter_interview_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='grade',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]