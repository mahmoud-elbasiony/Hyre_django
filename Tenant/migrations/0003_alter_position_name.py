# Generated by Django 4.2.2 on 2023-06-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tenant', '0002_alter_interview_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]